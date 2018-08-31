.DEFAULT_GOAL := help

.PHONY: image-build
image-build: scripts-image-build  ## Build container image from the package

.PHONY: image-clean
image-clean: scripts-image-clean  ## Clean old container images from local machine

.PHONY: image-deploy
image-deploy: scripts-image-release  ## Push container image built from the package to a remote image repository

.PHONY: scripts-image-%
scripts-image-%:
	@scripts/image-$*

.PHONY: lint
lint:  ## Run linters on package source code
	@scripts/lint

.PHONY: release-patch
release-patch: scripts-release-patch  ## Release package with next patch version, e.g. 0.0.2 -> 0.0.3

.PHONY: release-minor
release-minor: scripts-release-minor  ## Release package with next minor version, e.g. 0.2.1 -> 0.3.1

.PHONY: release-major
release-major: scripts-release-major  ## Release package with next major version, e.g. 2.1.1 -> 3.1.1

.PHONY: scripts-release-%
scripts-release-%:
	@scripts/release $*

.PHONY: test
test: test-unit test-integration test-interface  ## Run all package tests

.PHONY: test-unit
test-unit: scripts-test-unit  ## Run package unit tests

.PHONY: test-integration
test-integration: scripts-test-integration  ## Run package integration tests

.PHONY: test-interface
test-interface: scripts-test-interface  ## Run package interface (API, GUI) tests

.PHONY: scripts-test-%
scripts-test-%:
	@scripts/test-$* $(TEST)

.PHONY: help
help: ## Print Makefile usage.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
