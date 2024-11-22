# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Installation

```bash
poetry install
```

## Usage

There are four separate pipelines for the {{cookiecutter.project_name}} model:

- `preprocessing`: Fetches and preprocesses the data required for the model.
- `feature_engineering`: Performs feature engineering on the preprocessed data.
- `modelling`: Trains and evaluates the model.
- `postprocessing`: Performs postprocessing on the model's predictions, and writes the results to a database, etc.

Each of these pipelines can be run individually, or all of them can be run together. To run each one separately, use
the following commands:

- Preprocessing: `poetry run python -m {{cookiecutter.project_slug}}.preprocessing`
- Feature engineering: `poetry run python -m {{cookiecutter.project_slug}}.feature_engineering`
- Modelling: `poetry run python -m {{cookiecutter.project_slug}}.modelling`
- Postprocessing: `poetry run python -m {{cookiecutter.project_slug}}.postprocessing` The pipelines have various
  command-line arguments that can be used to customize their behavior. To find out more, run
  `poetry run python -m {{cookiecutter.project_slug}} --help`.

To run all of the pipelines together, use the following command:

```bash
poetry run python -m {{cookiecutter.project_slug}}
```

The command-line arguments for each pipeline can be pass in the form `--<pipeline-name>.<argument-name>`, e.g.

```bash
poetry run python -m {{cookiecutter.project_slug}} \
  --preprocessing.data_path /path/to/data \
  --feature_engineering.data_path /path/to/data \
  ... etc.
```

## License

{{cookiecutter.project_name}} is licensed under the {{cookiecutter.project_license}} license.
