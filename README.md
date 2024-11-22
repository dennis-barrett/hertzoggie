# Hertzoggie

Hertzoggie is a collection of cookiecutter templates, particularly for Python projects. These templates are quite
opinionated, and are tailored to my specific likes and needs (but others may find they like the structure). In
particular:

- They follow a specific folder structure.
- Poetry is used for dependency management.
- Ruff and Pyright are used for linting and type checking, respectively. Moreover, the generated `pyproject.toml`
  contains settings for these tools that I tend to use on all of my Python projects.

## Usage

First, install cookiecutter:

```bash
pip install cookiecutter
```

Then, use cookiecutter to generate a new project using a Hertzoggie template:

```bash
cookiecutter https://github.com/dennis-barrett/hertzoggie.git --directory="template-name"
```

(Here `template-name` is one of the template types described in the next section.) After following the prompts, the
project will be generated in the current directory.

## Templates

There are currently two templates:

- `py-pkg`: This is a basic Python package template. It includes a `pyproject.toml` file, a `poetry.lock` file, and a
  `README.md` file, and a very light folder structure.
- `py-ds`: This is a Python package template for data science projects specifically. In addition to the features of the
  `py-pkg` template, it has a more developed folder structure according to how my data science projects are typically
  organised.

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
