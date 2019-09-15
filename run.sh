#! /bin/sh
dockerd &
sleep 5s
docker pull python:3.6.5-alpine
ncat -vc 'python3 judge.py' -kl 0.0.0.0 9487
