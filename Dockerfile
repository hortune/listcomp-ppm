FROM docker:stable-dind

LABEL maintainer "lalalala"

RUN apk update &&\
    apk upgrade --no-cache &&\
    apk add --no-cache python libffi openssl &&\
    apk add --no-cache --virtual .build-deps python3-dev py-pip libffi-dev openssl-dev gcc libc-dev make 

RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi


RUN pip3 install epicbox &&\
    apk add --no-cache nmap-ncat &&\
    apk del .build-deps

RUN mkdir /ctf

COPY * /
EXPOSE 9487
ENTRYPOINT "/run.sh"
