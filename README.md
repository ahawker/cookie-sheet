# cookie-sheet

Create repositories from [Cookiecutter](https://github.com/audreyr/cookiecutter) templates that conform to the [Common Repository Interface](https://github.com/ahawker/common-repository-interface).

## Status

This repository is under active development.

## Goals

* "One-click" repository creation from Cookiecutter templates
* Cookiecutter templates that conform to the [Common Repository Interface](https://github.com/ahawker/common-repository-interface)
* Integration with [Dockerfiles](https://github.com/ahawker/dockerfiles)
* Integration with [Dotfiles](https://github.com/ahawker/dotfiles)
* Mechanism to share files between Cookiecutter templates (not officially supported)

## Usage

TODO

## Turtles all the way down...

This repository is contains the functionality for using Cookiecutter templates to create new repositories.
The templates enforce the [Common Repository Interface](https://github.com/ahawker/common-repository-interface). However,
since this repository is responsible for encapsulating all of the Cookiecutter work, it itself cannot be created via a Cookiecutter template without
endless recursion (I think).

Therein lies the rub.

This repository should still conform to the [Common Repository Interface](https://github.com/ahawker/common-repository-interface) to the best of its ability.

## Links

* Cookiecutter - https://github.com/audreyr/cookiecutter
* Common Repository Interface - https://github.com/ahawker/common-repository-interface

## License

* [Apache 2.0](LICENSE)
