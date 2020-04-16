FROM ubuntu:16.04

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN pip install sagemaker-containers

RUN pip install -r requirements

ENV PATH="/opt/program:$(PATH}"

COPY . /opt/program
WORKDIR /opt/program