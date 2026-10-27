# Diana API Python Examples

[English](README.md) | [中文](README.cn.md)

面向 **Diana / Thor 系列机器人**客户的 Python API 入门教程与可运行例程。

目标：客户下载仓库后，拉取官方 Diana Python SDK 子模块，选择机器人型号并传入 IP，即可从连接、状态读取开始逐步学习常用 API。

> 本仓库不重新封装一套机器人 SDK。`examples/` 尽量直接调用原始 Diana Python API；`common/` 只放参数解析、回调、等待、打印、SDK 加载和型号校验等公共辅助代码。

## 支持型号

```text
Diana series (7 axes)
├── Diana3       -> --model diana3
├── Diana7       -> --model diana7
└── Diana7 G2    -> --model diana7-g2

Thor series (6 axes)
├── Thor7        -> --model thor7
├── Thor12       -> --model thor12
└── Thor20       -> --model thor20
```

所有型号共用同一套 examples。型号差异集中在 [`robots/`](robots/) 中，连接后通过 `getJointCount()` 校验 7 轴 Diana / 6 轴 Thor。

## 导航入口

- [教程目录](docs/README.cn.md)
- [Python 冒烟测试说明](docs/platform_compatibility_test.cn.md)
- [01 连接与型号识别](examples/01_connection/README.cn.md)
- [02 机器人状态与诊断](examples/02_robot_state/README.cn.md)
- [03 关节运动](examples/03_joint_motion/README.cn.md)
- [04 笛卡尔运动](examples/04_cartesian_motion/README.cn.md)
- [05 运动学](examples/05_kinematics/README.cn.md)
- [06 I/O](examples/06_io/README.cn.md)
- [07 TCP、坐标系与负载](examples/07_tcp_and_frames/README.cn.md)
- [08 运动限制](examples/08_motion_limits/README.cn.md)
- [09 路径与路点](examples/09_path_and_waypoints/README.cn.md)
- [10 点动运动](examples/10_jog_motion/README.cn.md)
- [11 力阈值停止](examples/11_force_guarded_motion/README.cn.md)
- [12 ServoL 实时下发](examples/12_servoL_realtime/README.cn.md)

## 仓库内容

| 路径 | 说明 |
|---|---|
| [`examples/`](examples/) | 可运行 Python 示例。运动示例默认 dry-run，只有传入 `--run` 才发送运动命令。 |
| [`common/`](common/) | 示例公共辅助代码。 |
| [`robots/`](robots/) | 机器人型号 profile 和 registry。 |
| [`docs/`](docs/) | 教程、安全说明、FAQ 与验证说明。 |
| [`third_party/diana_sdk_python/`](third_party/diana_sdk_python/) | DianaApi Python SDK 子模块位置。 |

## SDK 准备

首次克隆时请带上子模块：

```bash
git clone --recurse-submodules <your-repo-url>
cd diana-api-examples-python
```

若主仓库已经克隆完成，再执行：

```bash
git submodule update --init --recursive
```

子模块已经包含适用于 Linux x86_64 的 SDK 3.3.0 原生运行库。运行例程前设置 Python wrapper 和原生动态库搜索路径：

```bash
export PYTHONPATH="$PWD/third_party/diana_sdk_python/lib:$PYTHONPATH"
export LD_LIBRARY_PATH="$PWD/third_party/diana_sdk_python/lib:$LD_LIBRARY_PATH"
```

需要使用不在 `third_party/` 下的 SDK 时，把环境变量 `DIANA_SDK_DIR` 设为该 SDK 目录（其中包含 `lib/`），并让 `PYTHONPATH` 与 `LD_LIBRARY_PATH` 指向它的 `lib/`：

```bash
export DIANA_SDK_DIR=/path/to/diana_sdk_python
export PYTHONPATH="$DIANA_SDK_DIR/lib:$PYTHONPATH"
export LD_LIBRARY_PATH="$DIANA_SDK_DIR/lib:$LD_LIBRARY_PATH"
```

## 第一个程序

查看支持型号：

```bash
python3 examples/01_connection/main.py --list-models
```

连接 Diana7：

```bash
python3 examples/01_connection/main.py --model diana7 --ip 192.168.10.75
```

连接 Thor12：

```bash
python3 examples/01_connection/main.py --model thor12 --ip 192.168.10.75
```

连接前先确认 PC 与机器人处于同一网段：

```bash
ping 192.168.10.75
```

## 安全

运动示例默认只计算并打印目标，不发送运动命令。

真正运动时要求显式指定 `--model`：

```bash
python3 examples/03_joint_motion/main.py --model diana7 --ip 192.168.10.75 --run
python3 examples/04_cartesian_motion/main.py --model thor12 --ip 192.168.10.75 --run
```

程序连接后还会调用 `getJointCount()` 校验轴数。运行前请阅读 [`docs/11_safety.cn.md`](docs/11_safety.cn.md)。

## 冒烟测试

执行不连接机器人的仓库自检：

```bash
python3 scripts/check_repository.py
```

脚本会检查 Python 语法、SDK 方法引用、本地 Markdown 链接、中英文档配对，以及每个例程的 `--list-models` 路径；不会验证机器人通信或真实运动。

## 文档依据

例程接口和教程主要依据《思灵机器人工业版 API 手册（Python 版）》及 Diana 控制接口文档整理。请以客户实际安装 SDK 版本对应的正式 API 手册为最终依据。


## 兼容性

| 示例版本 | SDK 版本 | SDK `version` 文件 |
|---|---|---|
| 1.0.0 | 3.3.0 | `industry-v3.3.0.260211` |

SDK 子模块固定到上表对应的 SDK tag。需要使用其他 SDK 版本时，请参阅“SDK 准备”，并在使用前自行验证示例。

## 许可证

本仓库的示例源码采用 MIT 许可证，见 [`LICENSE`](LICENSE)。作为子模块引用的 Diana SDK 是独立仓库，不在本许可证范围内。
