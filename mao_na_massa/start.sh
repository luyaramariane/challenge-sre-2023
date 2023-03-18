#!/bin/bash

docker stop challengeApp
docker rm challengeApp

sleep 1

docker build -t challengesre2023 --pull --force-rm . 

sleep 1

docker run --name challengeApp -p 5001:5000 -d challengesre2023:latest

sleep 1

docker ps

sleep 1

xdg-open http://localhost:5001/
