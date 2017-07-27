TAG?=v0.1
REGISTRY?=gcr.io/agarwalrohit-sandbox
IMAGE=tensorflow

build:
	docker build --pull -t ${REGISTRY}/${IMAGE}:${TAG} .

push:
	gcloud docker -- push ${REGISTRY}/${IMAGE}:${TAG}

.PHONY: build push
