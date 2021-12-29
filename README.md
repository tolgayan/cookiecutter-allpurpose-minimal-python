# cookiecutter-allpurpose-minimal-python

A simple cookiecutter template for general-purpose python projects.


## Managing dependencies

To start, run `poetry install`. This command will install all the packages I add to the dependencies as an initial start.

To add a pip package, run `poetry add <package name>`. This command will add the package to `pyproject.toml` file, and also
will install it to the environment.

Configurations for packages such as black, isort, pylint etc. can be set in `pyproject.toml` file.


## How to run

To run a command in the environment, add `poetry run` to the beginning of that command.

Example:

```bash
$poetry run python main.py <args>  # to run main.py 
$poetry run black                  # to run black 
$poetry run pylint src/ 
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

## Tests

An example test case is added into `tests` folder. You can run tests using the following code:

```bash
$poetry run pytest tests/
```
