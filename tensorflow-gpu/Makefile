TAG?=v0.3
REGISTRY?=gcr.io/agarwalrohit-sandbox
IMAGE=tensorflow-gpu

build:
	docker build --pull -t ${REGISTRY}/${IMAGE}:${TAG} .

push:
	gcloud docker -- push ${REGISTRY}/${IMAGE}:${TAG}

.PHONY: build push
