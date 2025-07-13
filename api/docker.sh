#!/bin/bash

# Docker helper script for Image Gallery API

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions
print_usage() {
    echo "Usage: $0 {build|run|stop|logs|clean|prod-build|prod-run}"
    echo ""
    echo "Commands:"
    echo "  build       Build development Docker image"
    echo "  run         Run development container"
    echo "  stop        Stop and remove container"
    echo "  logs        Show container logs"
    echo "  clean       Remove image and container"
    echo "  prod-build  Build production Docker image"
    echo "  prod-run    Run production container"
    echo ""
}

build_dev() {
    echo -e "${GREEN}Building development Docker image...${NC}"
    docker build -t image-gallery-api .
}

build_prod() {
    echo -e "${GREEN}Building production Docker image...${NC}"
    docker build -f Dockerfile.prod -t image-gallery-api:prod .
}

run_dev() {
    echo -e "${GREEN}Running development container...${NC}"
    docker run -d -p 5000:5000 --name image-gallery-api-dev --env-file .env.local image-gallery-api
    echo -e "${GREEN}Container started! API available at http://localhost:5000${NC}"
}

run_prod() {
    echo -e "${GREEN}Running production container...${NC}"
    docker run -d -p 5000:5000 --name image-gallery-api-prod --env-file .env.local image-gallery-api:prod
    echo -e "${GREEN}Production container started! API available at http://localhost:5000${NC}"
}

stop_container() {
    echo -e "${YELLOW}Stopping containers...${NC}"
    docker stop image-gallery-api-dev 2>/dev/null || true
    docker stop image-gallery-api-prod 2>/dev/null || true
    docker rm image-gallery-api-dev 2>/dev/null || true
    docker rm image-gallery-api-prod 2>/dev/null || true
    echo -e "${GREEN}Containers stopped and removed${NC}"
}

show_logs() {
    echo -e "${GREEN}Container logs:${NC}"
    docker logs image-gallery-api-dev 2>/dev/null || docker logs image-gallery-api-prod 2>/dev/null || echo "No running containers found"
}

clean_all() {
    echo -e "${YELLOW}Cleaning up Docker resources...${NC}"
    stop_container
    docker rmi image-gallery-api 2>/dev/null || true
    docker rmi image-gallery-api:prod 2>/dev/null || true
    echo -e "${GREEN}Cleanup complete${NC}"
}

# Main script
case "$1" in
    build)
        build_dev
        ;;
    run)
        run_dev
        ;;
    stop)
        stop_container
        ;;
    logs)
        show_logs
        ;;
    clean)
        clean_all
        ;;
    prod-build)
        build_prod
        ;;
    prod-run)
        run_prod
        ;;
    *)
        print_usage
        exit 1
        ;;
esac
