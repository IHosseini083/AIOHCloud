# Contributing

Thank you for being interested in contributing to AIOHCloud.
There are many ways you can contribute to the project:

- Try AIOHCloud and [report bugs/issues you find](https://github.com/IHosseini083/AIOHCloud/issues/new)
- Implement new features
- [Review Pull Requests of others](https://github.com/IHosseini083/AIOHCloud/pulls)
- Write documentation

## Reporting Bugs or Other Issues

Try to be more descriptive as you can and in case of a bug report,
provide as much information as possible, for example:

- OS platform
- Python version
- Installed dependencies and versions (`python -m pip freeze`)
- Code snippet
- Error traceback

You should always try to reduce any examples to the *simplest possible case*
that demonstrates the issue.

## Development

Prerequisites:

- [Python](https://python.org/) version 3.8 or later.
- [Poetry](https://python-poetry.org/ 'Python packaging and dependency management system')
version 1.2.2 (or later) for dependency management. You should know basic stuff about handling dependencies using poetry command line interface.

To start developing AIOHCloud, create a **fork** of the
[AIOHCloud repository](https://github.com/IHosseini083/AIOHCloud) on GitHub.

Then clone your fork with the following command replacing `YOUR-USERNAME` with
your GitHub username:

```shell
git clone https://github.com/YOUR-USERNAME/AIOHCloud
```

You can now install the project and its dependencies using:

```shell
cd AIOHCloud
$ sudo chmod +x scripts/*
$ scripts/install
```

**Note**: After installing all the dependencies, you need to run the bellow command to enable [pre-commit]:

```shell
pre-commit install
```

## Testing and Linting

We use custom shell scripts to automate testing, linting,
and documentation building workflow.

To run the tests, use:

```shell
scripts/test
```

Any additional arguments will be passed to `pytest`. See the [pytest documentation](https://docs.pytest.org/en/latest/how-to/usage.html) for more information.

For example, to run a single test script:

```shell
scripts/test tests/test_application.py
```

To run the code auto-formatting:

```shell
scripts/lint
```

Lastly, to run code checks separately (they are also run as part of `scripts/test`), run:

```shell
scripts/check
```

## Documenting

Documentation pages are located under the `docs/` folder.

To run the documentation site locally (useful for previewing changes), use:

```shell
scripts/docs
```

## Releasing

*This section is targeted at AIOHCloud maintainers.*

Before releasing a new version, create a pull request that includes:

- **An update to the changelog**:
  - We follow the format from [keepachangelog](https://keepachangelog.com/en/1.0.0/).
  - [Compare](https://github.com/IHosseini083/AIOHCloud/compare/) `main` with the tag of the latest release, and list all entries that are of interest to our users:
    - Things that **must** go in the changelog: added, changed, deprecated or removed features, and bug fixes.
    - Things that **should not** go in the changelog: changes to documentation, tests or tooling.
    - Try sorting entries in descending order of impact / importance.
    - Keep it concise and to-the-point. 🎯
- **A version bump**: see `aiohcloud\__init__.py`.

Once the release PR is merged, create a
[new release](https://github.com/IHosseini083/AIOHCloud/releases/new) including:

- Tag version like `v0.13.3`.
- Release title `Version 0.13.3`
- Description copied from the changelog.

Once created this release will be automatically uploaded to PyPI.

<p align="center">
    <em>
    Partially taken from <a href="https://github.com/encode/starlette">Starlette</a>'s contribution guidelines.
    </em>
</p>

[pre-commit]: https://github.com/pre-commit/pre-commit "A framework for managing and maintaining multi-language pre-commit hooks."
