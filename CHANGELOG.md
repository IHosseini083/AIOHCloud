# ♻️ Changelog

All notable changes to this project will be documented in this file.

The format used in this document is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.0.7] - (2022-01-07)

### Added

- Add `json` parameter to `HetznerCloud.request` method for sending JSON data to the API.
- Add utility function to validate labels.
- Add tests for label validator.
- Add PyPI version badge.

### Changed

- Change string representation of `HetznerCloud` instances by overriding `Representation.__repr_args__` method.
- Turn `Handler` class into an ABC.
- Change dependabot interval for python packages to `daily`.
- Get recommended datacenter before iterating datacenters list, #4 by @IHosseini083.
- Improve `HetznerCloud` class type hints

### Removed

- Remove poetry pre-commit hook.

### Fixed

- Fix typo: `LABLES_` -> `LABELS_`.

## [0.0.3] - (2022-12-05)

### Added

- Add `Datacenters` handler for `/datacenters` endpoint.
- Add a simple example to docs and remove `Usage` section from first page.

### Changed

- Make `Paginated[T]` type a lazy iterator object.
- Renamed `models` module to `types`.
- Change documentation domain name to `aiohcloud.iliya.dev`.

### Fixed

- Fix a typo: `alos` -> `also`

## [0.0.2] - (2022-12-02)

### Added

- Add base API client and models.
- Add handler for `/actions` endpoint.
- Add CNAME file to support a custom domain for docs.

### Changed

- Update index page of docs and README.md file.

[0.0.2]: https://github.com/IHosseini083/AIOHCloud/releases/tag/v0.0.2
[0.0.3]: https://github.com/IHosseini083/AIOHCloud/compare/v0.0.2...v0.0.3
