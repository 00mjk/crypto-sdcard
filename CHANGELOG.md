# Changelog
All notable changes to *crypto-sdcard* since v1.7.1 will be documented in this file.

The format is based on [Keep a Changelog v1.1.0](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning v2.0.0](https://semver.org/spec/v2.0.0.html).

## 1.8.0 - [Unreleased]
### Changed
- Fix a couple of technical details denoted in the [CHANGELOG.md](https://github.com/Olf0/crypto-sdcard/blob/master/CHANGELOG.md).
- [Clean up some obsolete stuff](https://github.com/Olf0/crypto-sdcard/pull/246/commits).

## [1.7.2] - 2021-05-23
### Added
- [changelog-template.md](https://github.com/Olf0/crypto-sdcard/blob/master/changelog-template.md)
- [CHANGELOG.md](https://github.com/Olf0/crypto-sdcard/blob/master/CHANGELOG.md)
### Changed
- In the two files **[systemd/system](https://github.com/Olf0/crypto-sdcard/tree/master/systemd/system)/cryptosd-\*@%i.service**: [Omit `PartOf=mount-cryptosd-*@%i.service`](https://github.com/Olf0/crypto-sdcard/commit/c36150eb8a6ff99f9ab2376e1a41e82a3047afb9), as it does work as intended, but fails on boot-up.
### Removed
- No such item.<br />
  (Just keeping this section as a template, because it is part of the original template.)

## [Versions before 1.7.2] (2018 - 2021)
See [original thread at TJC](https://together.jolla.com/question/179054/how-to-creating-partitions-on-sd-card-optionally-encrypted/?answer=189813#post-id-189813), 
the [course version history in the README](https://github.com/Olf0/crypto-sdcard#version-history) and
the [detailed version specific release notes](https://github.com/Olf0/crypto-sdcard/releases?after=0.4-0).


[Unreleased]: https://github.com/Olf0/crypto-sdcard/compare/1.7.2...HEAD
[1.8.0]: https://github.com/Olf0/crypto-sdcard/compare/1.7.2...1.8.0
[1.7.2]: https://github.com/Olf0/crypto-sdcard/compare/1.7.1-1.sfos340regular...1.7.2
[Versions before 1.7.2]: https://github.com/Olf0/crypto-sdcard/releases?after=1.7.2
