TAG?=v0.1
REGISTRY?=gcr.io/agarwalrohit-sandbox
IMAGE=cuda-vector-add

build:
	docker build --pull -t ${REGISTRY}/${IMAGE}:${TAG} .

push:
	gcloud docker -- push ${REGISTRY}/${IMAGE}:${TAG}

.PHONY: build push
