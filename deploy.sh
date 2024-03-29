#!/bin/bash

docker compose up -d --build 

sleep 5

curl http://localhost:8080