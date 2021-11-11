#! /bin/bash

for i in {1..10}
do
    docker kill bash_container_${i}
    docker rm bash_container_${i}
done