#! /bin/bash

docker network create xd
for i in {1..10}
do
    docker run -d -t --name bash_container_${i} ubuntu
done