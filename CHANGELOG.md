# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.2] - 2023-11-15
### Added
 - `!dotabuff`/`!yasp` command
 - Utilities for dota matches (`scootbot3.util.dota.match`), heroes
   (`scootbot3.util.dota.heroes`), and Steam IDs (`scootbot3.constants.steam`).

### Changed
 - Reworked `test_listener` fixture factory to allow matching command output to
   an expected regex pattern instead of exact string equality.

## [3.0.1] - 2023-04-22
### Added
 - `!pickone` command

### Maintenance
 - Simplified requirements files: moved all dev and runtime deps from
   `requirements.in` files to `pyproject.toml`.
 - Rework tox testenvs to use tox-extras.
 - Refactored input-output test logic for listener into
   `tests/conftest.py::test_listener` fixture factory.

## [3.0.0] - 2023-04-16
Initial release.

[3.0.2]: https://github.com/sclabs/scootbot3.0/compare/v3.0.1...v3.0.2
[3.0.1]: https://github.com/sclabs/scootbot3.0/compare/v3.0.0...v3.0.1
[3.0.0]: https://github.com/sclabs/scootbot3.0/releases/tag/v3.0.0
