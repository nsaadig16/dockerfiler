![PyPI - Version](https://img.shields.io/pypi/v/dockerfiler)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dockerfiler)

<div align="center">
<img src="https://raw.githubusercontent.com/nsaadig16/dockerfiler/refs/heads/main/assets/icon.png" width=100 >
</div>

# DockerFiler

**Dockerfiler** is a tool that builds a Dockerfile given some interactive prompts.

## Installation

You can installing using `pip`:

```bash
pip install dockerfiler # Install the library
python3 dockerfiler # Run the tool
```

Alternatively, you can run it using `uvx`.

```bash
uvx dockerfiler # Run the tool without installing
```

## Usage

Run it via `pip` or `uvx`:

```bash
python3 dockerfiler # pip
uvx dockerfiler # uvx
```

Then follow the interactive prompts to select your project type and configure your Dockerfile.

## Supported project types

- Python (`uv`)
- Django (`uv`)
- FastAPI (`uv`)

## Requirements

- Python 3.12+
