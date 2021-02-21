# Contributing to the compiler

Instructions for contributing a recipe can be found [here](https://microsoft.github.io/DevCookbook/contribute/).

## How to clone and set up the repository

Please make a [fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) of the repository if you would like to make a contribution.

Clone your fork with `git clone`

``` bash
git clone https://github.com/<YOUR-GITHUB-USERNAME>/DevCookbook
```

### Linux

Create a virtual environment for installing packages

``` bash
python3.9 -m venv .venv
```

Activate the virtual environment

``` bash
source .venv/bin/activate
```

Install the required dependencies

``` bash
pip install -r requirements.txt
```

## Compile the site locally

``` bash
python compile.py -t dev
```