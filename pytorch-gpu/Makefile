TAG?=v0.4.0
REGISTRY?=gcr.io/agarwalrohit-sandbox
IMAGE=pytorch-gpu

build:
	docker build --pull -t ${REGISTRY}/${IMAGE}:${TAG} .

push:
	gcloud docker -- push ${REGISTRY}/${IMAGE}:${TAG}

.PHONY: build push
