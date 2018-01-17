FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

RUN apt-get update && \
    apt-get install -y python-pip python-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install tensorflow-gpu==1.4.1

COPY ./matmul.py matmul.py
