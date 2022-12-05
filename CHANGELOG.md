# ♻️ Changelog

All notable changes to this project will be documented in this file.

The format used in this document is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

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
