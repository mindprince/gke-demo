FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

RUN apt-get update && \
    apt-get install -y python-pip python-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install tensorflow==1.5.0

COPY ./matmul.py matmul.py
