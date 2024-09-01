#!/bin/bash

# "Nuclear option" script that deletes every possible docker artifact on your machine.
#  Run at your own risk.



echo "Stopping all running Docker containers..."
docker stop $(docker ps -aq)

echo "Removing all Docker containers..."
docker rm $(docker ps -aq)

echo "Removing all Docker images..."
docker rmi $(docker images -q) --force

echo "Removing all Docker volumes..."
docker volume rm $(docker volume ls -q) --force

echo "Removing all Docker networks..."
docker network rm $(docker network ls -q) --force

echo "Pruning unused Docker data..."
docker system prune --all --force --volumes

echo "Docker cleanup complete."
