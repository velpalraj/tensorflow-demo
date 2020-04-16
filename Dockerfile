FROM ubuntu:16.04

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py

ENV PATH="/opt/program:$(PATH}"

COPY . /opt/program
WORKDIR /opt/program

RUN pip install -r requirements