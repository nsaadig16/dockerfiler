.PHONY: clean build test run check-version deploy

define printYellow
	@echo -e "\033[33m$(1)\033[0m"
endef

clean:
	$(call printYellow,Cleaning...)
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	rm -rf dist/ build/ README _files *.egg-info .venv *Dockerfile *.dockerignore
	uv cache clean

build: clean
	$(call printYellow,Building...)
	uv build --no-cache

test: build
	$(call printYellow,Creating fresh venv and installing...)
	uv venv --python 3.12
	uv pip install --no-cache dist/*.whl
	$(call printYellow,Testing installation...)
	.venv/bin/dockerfiler --help

run: test
	$(call printYellow,Running...)
	.venv/bin/dockerfiler --output-dockerfile "example.Dockerfile" --output-dockerignore "example.dockerignore"

check-version:
	$(call printYellow,Current version in pyproject.toml:)
	@LOCAL_VERSION=$$(grep "^version" pyproject.toml | sed 's/version = "\(.*\)"/\1/'); \
	echo $$LOCAL_VERSION; \
	echo -e "\033[33mLatest version on PyPI:\033[0m"; \
	PYPI_VERSION=$$(pip index versions dockerfiler 2>/dev/null | grep -oP 'Available versions: \K[0-9.]+' | head -1); \
	echo $$PYPI_VERSION; \
	if [ "$$LOCAL_VERSION" = "$$PYPI_VERSION" ]; then \
		echo -e "\033[31mERROR: Version $$LOCAL_VERSION already exists on PyPI!\033[0m"; \
		echo -e "\033[31mPlease update the version in pyproject.toml before deploying.\033[0m"; \
		exit 1; \
	else \
		echo -e "\033[33mVersion check passed: $$LOCAL_VERSION is new\033[0m"; \
	fi

deploy: check-version build
	$(call printYellow,Updating lockfile...)
	uv lock
	$(call printYellow,Preparing to deploy...)
	@sleep 10
	uv publish && uv cache clean