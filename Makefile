IMAGE := ericsperano/dougiebot
VERSION := $(shell awk -F \' '{print $$2}' dougiebot/version.py)

.DEFAULT_GOAL := build

build:
	docker build -t $(IMAGE):$(VERSION) . --squash

tag: build
	docker tag $(IMAGE):$(VERSION) $(IMAGE):latest
	git tag -a v$(VERSION) -m "Version $(VERSION)"

publish: tag
	docker push $(IMAGE):$(VERSION)
	docker push $(IMAGE):latest

git_publish:
	git push origin v$(VERSION)
