# Opinionated Python Library Cookiecutter Template

This repository contains a template for Python libraries using Sphinx with integrated linting and GitHub Actions for export to GitHub Pages.

## Features

- **Makefile installation, testing, exporting, linting, and documentation**
- **Optional automatic documentation export to GitHub Pages**

## Creation

First, install `cookiecutter` and `jinja2-time`,

```bash
pip install cookiecutter jinja2-time
```

Then, use the template to create a new project folder using the following command, filling out the template naming and optional information as desired,

```bash
cookiecutter gh:oafish1/library-templatecookiecutter
```

Your project is now created! Feel free to begin development.

## Usage

To export documentation and requirements, make sure that you have `make` installed for your operating system, then install required dependencies.

```bash
make install  # Install your library in development mode
make install-dev  # Install your library with development requirements, including for documentation and dependency logging
```

Here is a summary of the usable make commands,

```bash
make build  # Record environment requirements.txt and requirements-dev.txt
make build-docs  # Build documentation using sphinx, may need to delete `docs/source/api`
make test  # Run unit tests
make lint  # Lint existing code
make pre-commit  # Run build, build-docs, lint, then test
```

Note that the template also includes an optional mechanism to automatically generate documentation on a `docs` branch using GitHub Actions.
