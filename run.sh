#!/bin/bash

NAME="main"

cd docker && \
docker-compose up  --build && \
docker rm docker_${NAME}_1
