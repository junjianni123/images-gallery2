# Docker helper script for React Frontend (PowerShell)

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

function Build-DevImage {
    Write-ColorText "Building development Docker image..." "Green"
    docker build -t image-gallery-frontend .
}

function Build-ProdImage {
    Write-ColorText "Building production Docker image..." "Green"
    docker build -f Dockerfile.prod -t image-gallery-frontend:prod .
}

function Run-DevContainer {
    Write-ColorText "Running development container..." "Green"
    docker run -d -p 3000:3000 --name image-gallery-frontend-dev `
        -e REACT_APP_API_URL=http://localhost:5000 `
        -v ${PWD}:/app `
        -v /app/node_modules `
        image-gallery-frontend
    Write-ColorText "Container started! Frontend available at http://localhost:3000" "Green"
}

function Run-ProdContainer {
    Write-ColorText "Running production container..." "Green"
    docker run -d -p 80:80 --name image-gallery-frontend-prod `
        -e REACT_APP_API_URL=http://localhost:5000 `
        image-gallery-frontend:prod
    Write-ColorText "Production container started! Frontend available at http://localhost" "Green"
}

function Stop-Containers {
    Write-ColorText "Stopping containers..." "Yellow"
    try { docker stop image-gallery-frontend-dev 2>$null } catch {}
    try { docker stop image-gallery-frontend-prod 2>$null } catch {}
    try { docker rm image-gallery-frontend-dev 2>$null } catch {}
    try { docker rm image-gallery-frontend-prod 2>$null } catch {}
    Write-ColorText "Containers stopped and removed" "Green"
}

function Show-ContainerLogs {
    Write-ColorText "Container logs:" "Green"
    try {
        docker logs image-gallery-frontend-dev 2>$null
    } catch {
        try {
            docker logs image-gallery-frontend-prod 2>$null
        } catch {
            Write-Host "No running containers found"
        }
    }
}

function Clean-Resources {
    Write-ColorText "Cleaning up Docker resources..." "Yellow"
    Stop-Containers
    try { docker rmi image-gallery-frontend 2>$null } catch {}
    try { docker rmi image-gallery-frontend:prod 2>$null } catch {}
    Write-ColorText "Cleanup complete" "Green"
}

# Main script execution
switch ($Command) {
    "build" { Build-DevImage }
    "run" { Run-DevContainer }
    "stop" { Stop-Containers }
    "logs" { Show-ContainerLogs }
    "clean" { Clean-Resources }
    "prod-build" { Build-ProdImage }
    "prod-run" { Run-ProdContainer }
    default { Show-Usage }
}
