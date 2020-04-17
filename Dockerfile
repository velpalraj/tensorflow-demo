FROM ubuntu:16.04

# Install dependencies
RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && \
    pip install --no-cache-dir -r requirements.txt

ENV PATH="/opt/program:$(PATH}"

COPY . /opt/program
WORKDIR /opt/program
