#!/bin/bash

# This script runs a Redis server in a Docker container.
# Ensure Docker is installed and running before executing this script.
# Pull the latest Redis image from Docker Hub
docker pull redis:latest
# Run the Redis container in detached mode, mapping port 6379  
# to the host machine's port 6379
docker run -d -p 6379:6379 redis

# chmod +x run_redis.sh
