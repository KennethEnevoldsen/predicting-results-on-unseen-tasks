# Predicting Perfromance on Unseen Tasks

a WIP


# Setting the project up for development

This project is managed using a makefile that contains on the commonly run arguments workflows. And uses [uv](https://docs.astral.sh/uv/) for managing
dependencies.

To install uv use:
```bash
make install-uv
```

## Managing Dependencies

To install dependencies and create virtual environment run
```bash
make install
```

To add a dependency simply run:

```bash
uv add {package-name}
```

## Linting
For linting this project uses [ruff](https://docs.astral.sh/ruff/). You can run the linter using:

```py
make lint
```