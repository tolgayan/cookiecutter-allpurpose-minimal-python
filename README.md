# cookiecutter-allpurpose-minimal-python

A simple cookiecutter template for general-purpose python projects.

To use, run

```bash
pip install cookiecutter
cookiecutter https://github.com/tolgayan/cookiecutter-allpurpose-minimal-python
```


## Managing dependencies

Note: This template uses poetry. But if you want to use another tool for dependency management (pipenv, virtualenv, conda etc.), you can skip this section
and use your own tool. You can also delete `pyproject.toml` file. No part of the template depends on poetry. But it may be easier to manage your environment, and
to configure the tools such as black or pylint wıth poetry. 


To start, run `poetry install`. This command will install all the packages I add to the dependencies as an initial start.

To add a pip package, run `poetry add <package name>`. This command will add the package to `pyproject.toml` file, and also
will install it to the environment.

Configurations for packages such as black, isort, pylint etc. can be set in `pyproject.toml` file.


## How to run

To run a command in the environment, add `poetry run` at the beginning of that command.

Example:

```bash
poetry run python main.py <args>  # to run main.py 
poetry run black                  # to run black 
poetry run pylint src/ 
```


## Logging

A basic logging configuration is added to the project. You can modify it from `logger.py` module. You can use
logger by adding the following code to any python file. The logger will use the settings in the `logger.py` file.

```python
import logging
logger = logging.getLogger(__name__)

# logging in code
logger.info('info log')
logger.warning('warning log')
logger.error('error log')
```

The logs will be shown in terminal, and will be saved into `artifacts/logs/<timestamp>.log`

## Tests

An example test case is added into `tests` folder. You can run tests using the following code:

```bash
poetry run pytest tests/
# or
poetry run pytest
```
