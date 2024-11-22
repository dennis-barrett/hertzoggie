# Hertzoggie

Hertzoggie is a collection of cookiecutter templates, particularly for Python projects.

## Usage

First, install cookiecutter:

```bash
pip install cookiecutter
```

Then, use cookiecutter to generate a new project using a Hertzoggie template:

```bash
cookiecutter https://github.com/dennis-barrett/hertzoggie.git --directory="template-name"
```

Here `template-name` is one of the template types described in the next section.

## Templates

There are currently two templates:

- `py-pkg`
- `py-ds`

## Development

To work on the Hertzoggie templates themselves there is a `pyproject.toml` file intended for use with Poetry. First,
initialise the Poetry virtual environment from within the Hertzoggie root directory:

```bash
poetry shell
```

Then install the dependencies; in particular this will install `cookiecutter` into the virtual environment:

```bash
poetry install
```

The `cookiecutter` installed in the virtual environment can then be used as described in the Usage section of this
document.
