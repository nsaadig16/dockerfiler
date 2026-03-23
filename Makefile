.PHONY: test clean

test:
	uv run dockerfiler --output "example.Dockerfile"
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf dist/ *.egg-info