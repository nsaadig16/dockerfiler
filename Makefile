.PHONY: build test clean deploy

build: clean
	uv build
deploy: build
	uv publish && uv cache clean
test:
	uv sync && uv run dockerfiler --output "example.Dockerfile"
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf dist/ *.egg-info