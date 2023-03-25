# airflow-dags

## Local setup

### Requirements and setup

#### Set up your virtualenv and install the Python requirements

```shell
python -m venv venv
. venv/bin/activate
pip install -r requirements
```

#### Install `pre-commit` and `allure`

`pre-commit` will ensure the git hooks run on commit. This includes `black`, `flake`, `pytest`, etc. On MacOS,
you can install these with `brew`. Refer to https://pre-commit.com/#install as needed for installation instructions.
`pre-commit` will install some git-ignored sample hooks in `.git/hooks`

```shell
brew install pre-commit  # or equivalent
brew install allure
```

#### Add `.githooks` to your git config
By default, the hooks path is `.git/hooks`. Since `.git` is ignored (and we want to share our hooks!),
we use `.githooks`
```shell
git config core.hooksPath .githooks
```

### Formatting, Linting and Testing
Formatting is handled by `black`, a "hightly opionated" Python formatter. 
> Sometimes, running Black with its defaults and passing filepaths to it just won’t cut it.  

For those cases, feel free to tweak the config. You can read more here: https://black.readthedocs.io/en/stable/usage_and_configuration/

Linting is handled by `flake8`, whose config is in `.flake8`. Similarly, this
can be overly strict. Feel free to tweak the config as necessary: https://flake8.pycqa.org/en/latest/user/configuration.html

Pytest is handled locally by `pytest`. The `pytest` config is stored in `pytest.ini`, which you can read more about here:  https://docs.pytest.org/en/7.1.x/reference/customize.html

