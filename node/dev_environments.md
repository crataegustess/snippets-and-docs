# Setting up dev environments for node / js

**caveat** These tips are for mac users and may help linux and windows users but check your own mileage

## multiple concurrent versions
The tool of choice is nvm. Installation can be a little tricky and involves an addition to .bashrc or .zshrc

[installation instructions](https://github.com/nvm-sh/nvm/blob/master/README.md)

- built in aliases for long term support versions
- can set up custom aliases
- per project version can be set in .nvmrc (just type `nvm use` in the folder to pick up)