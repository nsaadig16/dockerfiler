.PHONY: clean build test run check-version deploy

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	rm -rf dist/ build/ *.egg-info
build: clean
	uv build
test: build
	uv pip install dist/*.tar.gz --force-reinstall
	@echo "Testing installation..."
	dockerfiler --help
run: test
	dockerfiler --output-dockerfile "example.Dockerfile" --output-dockerignore "example.dockerignore"
check-version:
	@echo "Current version in pyproject.toml:"
	@grep "^version" pyproject.toml
deploy: check-version build
	@echo "Preparing to deploy..."
	@sleep 3
	uv publish && uv cache clean