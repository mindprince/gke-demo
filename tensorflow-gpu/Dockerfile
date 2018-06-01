FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

RUN apt-get update && \
    apt-get install -y python-pip python-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install tensorflow-gpu==1.8.0

COPY ./matmul.py matmul.py
