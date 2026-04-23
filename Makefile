.PHONY: clean build test run check-version deploy

define printYellow
	@echo -e "\033[33m$(1)\033[0m"
endef

clean:
	$(call printYellow,Cleaning...)
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	rm -rf Dockerfile .dockerignore dist/ build/ *.egg-info README_files
build: clean
	$(call printYellow,Building...)
	uv build
test: build
	uv pip install dist/*.tar.gz --force-reinstall
	$(call printYellow, Testing installation...)
	uvx --from dist/*.tar.gz dockerfiler --help
run: test
	$(call printYellow,Running...)
	uvx --from dist/*.tar.gz dockerfiler --output-dockerfile "example.Dockerfile" --output-dockerignore "example.dockerignore"
check-version:
	$(call printYellow,Current version in pyproject.toml:)
	@grep "^version" pyproject.toml
	$(call printYellow,Latest version available:)
	@pip index versions dockerfiler | grep dockerfiler
deploy: check-version build
	$(call printYellow,Updating lockfile...)
	uv lock
	$(call printYellow,Preparing to deploy...)
	@sleep 10
	uv publish && uv cache clean