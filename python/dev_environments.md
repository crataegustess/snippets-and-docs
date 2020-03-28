# Setting up dev environments for python

**caveat** These tips are for mac users and may help linux and windows users but check your own mileage

## multiple concurrent versions

### Setup pyenv
[getting started](https://github.com/pyenv/pyenv)

Make sure that the initialise steps and in .bashrc or .zshrc files

Use python.version within projects to pin to a specific version of python

### Use virtual environments
[getting started](https://realpython.com/python-virtual-environments-a-primer/)
[latest docs](https://docs.python.org/3/library/venv.html)

Feeling adventurous? use them both together [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

### (I don't use) pipenv
like pip but more... I don't use pipenv but this article contains some useful pip commands:
[pipenv article](https://docs.python-guide.org/dev/virtualenvs/)

### poetry
Oooh the new shiny for installation management and packaging, more shiny than PyPi even, maybe. Hit version 1 at start of 2020.

[poetry docs](https://python-poetry.org/docs/)

## what is the ideal set up for a project so someone new can pick it up quickly with lest instructions?
Still out for debate...