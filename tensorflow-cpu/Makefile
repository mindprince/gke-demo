TAG?=v0.4
REGISTRY?=gcr.io/agarwalrohit-sandbox
IMAGE=tensorflow-cpu

build:
	docker build --pull -t ${REGISTRY}/${IMAGE}:${TAG} .

push:
	gcloud docker -- push ${REGISTRY}/${IMAGE}:${TAG}

.PHONY: build push
