#! /bin/sh
dockerd &
sleep 5s
docker pull hortune/python3.6-alpine
ncat -vc 'timeout 777 python3 judge.py' -kl 0.0.0.0 9487
