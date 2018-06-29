FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install torch==0.4.0 torchvision==0.2.1

COPY ./matmul.py matmul.py
