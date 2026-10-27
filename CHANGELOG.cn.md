# 更新日志

[English](CHANGELOG.md) | [中文](CHANGELOG.cn.md)

## 1.0.0

- 首个版本：12 个 Python 示例，以及用于 SDK 加载、通用 CLI 参数、回调、运动等待、打印和机器人型号校验的 Python 支持模块。
- 添加 Diana3、Diana7、Diana7 G2、Thor7、Thor12 和 Thor20 机器人配置。
- 运动示例默认 dry-run；真实运动需要显式指定 `--model` 和 `--run`。
- 提供中英文顶层 README、文档页面、FAQ 和各示例 README。
- 新增环境变量 `DIANA_SDK_DIR`，可使用不在 `third_party/` 下的 SDK。
- 适配 SDK 3.3.0；`third_party/diana_sdk_python` 子模块固定到其 `v3.3.0` tag。
- 为本仓库的示例源码添加 MIT 许可证（`LICENSE`）。
