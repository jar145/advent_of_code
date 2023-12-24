
# Advent of Code

## Setup

1. Install Python3 using `asdf`.
1. Install poetry via `pipx` (`pipx` can be installed via brew): https://python-poetry.org/docs/#installing-with-pipx
1. Navigate into the project directory:
   ```zsh
   $ cd metrics
   ```
1. Create a new virtual environment:
   ```zsh
   $ python -m venv venv
   $ . venv/bin/activate (or source ./venv/bin/activate)
   ```
1. Install the required dependencies:
   ```zsh
   $ poetry install
   ```
1. Make a copy of the example environment variables file:
   ```zsh
   $ cp .env.example .env
   ```

1. Scripts can be in one of the following ways:
   - via python directly, for example:
      ```
      $ python src/metrics/tango_spring_starter_usage/tango_spring_starter_usage_metrics.py
      ```
   - or via poetry (see `pyproject.toml` for script definitions), for example
      ```
      $ poetry run tango-spring-starter-usage-metrics
      ```
      or merely use the poetry script name by itself
      ```
      $ tango-spring-starter-usage-metrics
      ```
