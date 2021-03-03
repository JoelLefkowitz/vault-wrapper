# Vault wrapper

Hvac wrapper to automate enabling kv engines

## Status

| Source     | Shields                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| Project    | ![release][release_shield] ![license][license_shield] ![dependents][dependents_shield]                             |
| Health     | ![travis][travis_shield] ![codacy][codacy_shield] ![coverage][coverage_shield] ![readthedocs][readthedocs_shield]  |
| Repository | ![issues][issues_shield] ![pulls][pulls_shield]                                                                    |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]           |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield] |

## Installation

```bash
pip install vault_wrapper
```

## Tests

To run unit tests:

```bash
grunt tests:unit
```

To generate a coverage report:

```bash
grunt tests:coverage
```

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

To generate the sphinx configuration:

```bash
grunt docs:generate
```

Then build the documentation:

```bash
grunt docs:build
```

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

Before commiting new code:

```bash
grunt precommit
```

This will run linters, formaters, generate a test coverage report and the sphinx configuration.

## Versioning

This repository adheres to semantic versioning standards.
For more inforamtion on semantic versioning visit [SemVer][semver].

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

## Changelog

Please read this repository's [CHANGELOG](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][joellefkowitz]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Github links -->

[pulls]: https://github.com/JoelLefkowitz/vault-wrapper/pulls
[issues]: https://github.com/JoelLefkowitz/vault-wrapper/issues

<!-- External links -->

[readthedocs]: https://vault-wrapper.readthedocs.io/en/latest/
[semver]: http://semver.org/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Acknowledgments -->

[joellefkowitz]: https://github.com/JoelLefkowitz

<!-- Project shields -->

[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/vault-wrapper
[license_shield]: https://img.shields.io/github/license/joellefkowitz/vault-wrapper
[dependents_shield]: https://img.shields.io/librariesio/dependent-repos/pypi/vault_wrapper

<!-- Health shields -->

[travis_shield]: https://img.shields.io/travis/joellefkowitz/vault-wrapper
[codacy_shield]: https://img.shields.io/codacy/coverage/vault-wrapper
[coverage_shield]: https://img.shields.io/codacy/grade/vault-wrapper
[readthedocs_shield]: https://img.shields.io/readthedocs/vault-wrapper

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/vault-wrapper
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/vault-wrapper

<!-- Publishers shields -->

[pypi_shield]: https://img.shields.io/pypi/v/vault_wrapper
[python_versions_shield]: https://img.shields.io/pypi/pyversions/vault_wrapper
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/vault_wrapper

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/vault-wrapper
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/vault-wrapper
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/vault-wrapper
