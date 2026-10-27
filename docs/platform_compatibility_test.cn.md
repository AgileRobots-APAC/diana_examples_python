# Python 冒烟测试

本仓库提供轻量冒烟测试，用于验证 Python 语法、公共 CLI 参数和不连接机器人的 `--list-models` 路径。

## 检查项

| 检查项 | 命令 | 是否连接机器人 |
|---|---|---|
| Python 语法检查 | `python3 -m py_compile common/*.py robots/*.py examples/*/main.py` | 否 |
| 型号列表 CLI | `for f in examples/*/main.py; do python3 "$f" --list-models >/dev/null; done` | 否 |

`--list-models` 在导入 DianaApi 原生库前退出，因此可用于没有连接机器人、甚至暂未准备原生动态库的环境。

## 本地冒烟测试

首次运行前初始化 SDK 子模块：

```bash
git submodule update --init --recursive
```

运行：

```bash
python3 -m py_compile common/*.py robots/*.py examples/*/main.py
for f in examples/*/main.py; do python3 "$f" --list-models >/dev/null; done
```

这些检查不会连接机器人，也不会执行 `--run`。

## 真机验证

冒烟测试通过只表示脚本和公共参数路径可用，不能证明实际网络通信或运动控制。

在目标 Ubuntu 的实体机或虚拟机上，先设置 SDK 路径：

```bash
export PYTHONPATH="$PWD/third_party/diana_sdk_python/lib:$PYTHONPATH"
export LD_LIBRARY_PATH="$PWD/third_party/diana_sdk_python/lib:$LD_LIBRARY_PATH"
```

然后依次运行：

```bash
python3 examples/01_connection/main.py --model diana7 --ip <robot-ip>
python3 examples/02_robot_state/main.py --model diana7 --ip <robot-ip>
```

接着验证全部默认 dry-run 示例。任何带 `--run` 的测试都必须在现场完成人员、速度、负载、净空与急停确认后手工执行。
