# common/partials/testing
#
# Makefile partial for test related functionality.

.DEFAULT_GOAL := help

TEST_SCRIPTS := $(sort $(wildcard scripts/test-*))

.PHONY: test
test: $(TEST_SCRIPTS)  ## Run all package tests

.PHONY: test-%
test-%: scripts/test-%  ## Run tests defined in the scripts/test-% script

.PHONY: $(TEST_SCRIPTS)
$(TEST_SCRIPTS):
	@echo "Running '$@' tests..."
	@$@ $(TEST)

.PHONY: usage
help: ## Print Makefile usage
	@awk 'BEGIN {FS = ":.*?## "} /^[\/%a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
