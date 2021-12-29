# cookiecutter-allpurpose-minimal-python

A simple cookiecutter template for general-purpose python projects.


## Managing dependencies

To start, run `poetry install`. This command will install all the packages I add to the dependencies as an initial start.

To add a pip package, run `poetry add <package name>`. This command will add the package to `pyproject.toml` file, and also
will install it to the environment.

Configurations for packages such as black, isort, pylint etc. can be set in `pyproject.toml` file.
