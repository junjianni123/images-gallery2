# Docker helper script for Image Gallery API (PowerShell)

param(
    [Parameter(Position=0)]
    [ValidateSet("build", "run", "stop", "logs", "clean", "prod-build", "prod-run", "help")]
    [string]$Command = "help"
)

function Write-ColorText {
    param([string]$Text, [string]$Color = "White")
    switch ($Color) {
        "Green" { Write-Host $Text -ForegroundColor Green }
        "Yellow" { Write-Host $Text -ForegroundColor Yellow }
        "Red" { Write-Host $Text -ForegroundColor Red }
        default { Write-Host $Text }
    }
}

function Show-Usage {
    Write-Host "Usage: .\docker.ps1 {build|run|stop|logs|clean|prod-build|prod-run}"
    Write-Host ""
    Write-Host "Commands:"
    Write-Host "  build       Build development Docker image"
    Write-Host "  run         Run development container"
    Write-Host "  stop        Stop and remove container"
    Write-Host "  logs        Show container logs"
    Write-Host "  clean       Remove image and container"
    Write-Host "  prod-build  Build production Docker image"
    Write-Host "  prod-run    Run production container"
    Write-Host ""
}

function Build-Dev {
    Write-ColorText "Building development Docker image..." "Green"
    docker build -t image-gallery-api .
}

function Build-Prod {
    Write-ColorText "Building production Docker image..." "Green"
    docker build -f Dockerfile.prod -t image-gallery-api:prod .
}

function Run-Dev {
    Write-ColorText "Running development container..." "Green"
    docker run -d -p 5000:5000 --name image-gallery-api-dev --env-file .env.local image-gallery-api
    Write-ColorText "Container started! API available at http://localhost:5000" "Green"
}

function Run-Prod {
    Write-ColorText "Running production container..." "Green"
    docker run -d -p 5000:5000 --name image-gallery-api-prod --env-file .env.local image-gallery-api:prod
    Write-ColorText "Production container started! API available at http://localhost:5000" "Green"
}

function Stop-Container {
    Write-ColorText "Stopping containers..." "Yellow"
    try { docker stop image-gallery-api-dev 2>$null } catch {}
    try { docker stop image-gallery-api-prod 2>$null } catch {}
    try { docker rm image-gallery-api-dev 2>$null } catch {}
    try { docker rm image-gallery-api-prod 2>$null } catch {}
    Write-ColorText "Containers stopped and removed" "Green"
}

function Show-Logs {
    Write-ColorText "Container logs:" "Green"
    try {
        docker logs image-gallery-api-dev 2>$null
    } catch {
        try {
            docker logs image-gallery-api-prod 2>$null
        } catch {
            Write-Host "No running containers found"
        }
    }
}

function Clean-All {
    Write-ColorText "Cleaning up Docker resources..." "Yellow"
    Stop-Container
    try { docker rmi image-gallery-api 2>$null } catch {}
    try { docker rmi image-gallery-api:prod 2>$null } catch {}
    Write-ColorText "Cleanup complete" "Green"
}

# Main script execution
switch ($Command) {
    "build" { Build-Dev }
    "run" { Run-Dev }
    "stop" { Stop-Container }
    "logs" { Show-Logs }
    "clean" { Clean-All }
    "prod-build" { Build-Prod }
    "prod-run" { Run-Prod }
    default { Show-Usage }
}
