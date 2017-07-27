FROM nvidia/cuda:8.0-devel-ubuntu16.04

RUN apt-get update && \
    apt-get install -y python-pip python-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade tensorflow-gpu

COPY ./gpu.py gpu.py
