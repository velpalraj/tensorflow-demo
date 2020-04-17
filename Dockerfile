FROM ubuntu:18.04

# Install dependencies
RUN apt-get update && apt-get install -yqq \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get update && apt-get install -yqq \
    python \
    python-pip \
    python-setuptools \
    python-dev

ENV PATH="/opt/program:$(PATH}"

COPY requirements.txt .
RUN /usr/bin/pip install --no-cache-dir -r requirements.txt

COPY . /opt/program
WORKDIR /opt/program

ENTRYPOINT ["python", "script.py"]