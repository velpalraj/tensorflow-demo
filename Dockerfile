FROM ubuntu:16.04

ARG SRC_BKT_NAME
ARG OUTPUT_BKT
ARG SM_ROLE

ENV SRC_BKT_NAME=${SRC_BKT_NAME}
ENV OUTPUT_BKT=${OUTPUT_BKT}
ENV SM_ROLE=${SM_ROLE}

# Install dependencies
RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py && python get-pip.py && \
    pip install --no-cache-dir -r requirements.txt

ENV PATH="/opt/program:$(PATH}"

COPY model /opt/program
WORKDIR /opt/program
