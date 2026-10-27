# Changelog

[English](CHANGELOG.md) | [中文](CHANGELOG.cn.md)

## 1.0.0

- Initial release: 12 Python examples, with Python support modules for SDK loading, common CLI options, callbacks, motion waiting, printing, and robot model validation.
- Add robot profiles for Diana3, Diana7, Diana7 G2, Thor7, Thor12, and Thor20.
- Keep motion examples dry-run by default; real motion requires an explicit `--model` and `--run`.
- Add bilingual top-level README files, documentation pages, FAQ, and per-example README files.
- Add the `DIANA_SDK_DIR` environment variable to use an SDK that is not in `third_party/`.
- Compatible with SDK 3.3.0; the `third_party/diana_sdk_python` submodule is pinned to its `v3.3.0` tag.
- Add the MIT License (`LICENSE`) for the example source in this repository.
