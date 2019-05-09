#!/bin/bash

screen -AmdS server  python multiserver.py 1
screen -ls
sleep 1
screen -AmdS client1 python algo_client.py 1
screen -ls
sleep 1
screen -AmdS client2 python algo_client.py 2
screen -ls
sleep 1
screen -AmdS client3 python algo_client.py 3
screen -ls
sleep 1
# python algo_client.py 4
screen -AmdS client4 python algo_client.py 4
sleep 5

rm -rf /tmp/uscreens/S-rafambp
./kill.sh multiserver.py