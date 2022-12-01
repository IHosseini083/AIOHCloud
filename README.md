<div align="center">
<h1><a href="https://github.com/IHosseini083/AIOHCloud"><b>AIOHCloud</b></a></h1>
<a href="https://github.com/IHosseini083/AIOHCloud/actions?query=workflow%3ARelease" target="_blank">
    <img src="https://github.com/IHosseini083/AIOHCloud/workflows/Release/badge.svg" alt="Release">
</a>
<a href="https://github.com/IHosseini083/AIOHCloud/actions/workflows/publish-docs.yml?query=event%3Apush+workflow%3A%22Publish+Docs%22+branch%3Amain" target="_blank">
    <img src="https://github.com/IHosseini083/AIOHCloud/actions/workflows/publish-docs.yml/badge.svg" alt="Docs">
</a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.8+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python">
</a>
<a href="https://github.com/psf/black">
    <img src="https://img.shields.io/static/v1?label=code%20style&message=black&color=black&style=flat" alt="Code Style: black">
</a>
<a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat" alt="pre-commit">
</a>
</div>

_AIOHCloud_ is an asynchronous python library for Hetzner Cloud API inspired from the [hcloud-python]
project and complies with Hetzner Cloud API standards mentioned in its [documentation](https://docs.hetzner.cloud).

Key features of _AIOHCloud_ are:

- It's fully type hinted and plays nicely with your IDE/Editor and preferred linters.
- Representing API types using Python objects to access their properties easily.
- Fully asynchronous operations via [httpx] framework.

## Requirements

_AIOHCloud_ requires you to have Python 3.8+ installed.

It alos uses the following external packages:

- [httpx] to send HTTP requests.
- [attrs] for creating API response models.

## Installation

## Usage

## License

This project is licensed under the terms of the [GPL-3.0] licence.

<p align="center">&mdash; ⚡ &mdash;</p>

<!-- Links -->

[GPL-3.0]: https://www.gnu.org/licenses/gpl-3.0.en.html "GNU General Public License v3.0"
[hcloud-python]: https://github.com/hetznercloud/hcloud-python/ "hcloud-python is a library for the Hetzner Cloud API."
[httpx]: https://github.com/encode/httpx "A next generation HTTP client for Python"
[attrs]: https://github.com/python-attrs/attrs "Python Classes Without Boilerplate"
