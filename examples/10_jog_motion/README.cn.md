# 10 Jog Motion

[English](README.md) | [中文](README.cn.md)

低速点动示例。默认模式为 J1 正向点动；通过 `--mode` 可选择另外两种 TCP 点动：

- `--mode joint`：J1 正向点动（默认）。
- `--mode tcp`：调用 `moveTcp_ex`，沿基坐标系 +X 平移。
- `--mode rotate`：调用 `rotationTCP`，绕基坐标系 +Z 旋转。

默认 dry-run；执行需要 `--model ... --run`，可用 `--duration=0.1..2.0` 限定时长。程序始终调用 `stop()` 和 `holdBrake()`。

```bash
python3 examples/10_jog_motion/main.py --model diana7 --ip 192.168.10.75
python3 examples/10_jog_motion/main.py --model diana7 --ip 192.168.10.75 --mode joint --duration=0.5 --run
python3 examples/10_jog_motion/main.py --model diana7 --ip 192.168.10.75 --mode tcp --duration=0.5 --run
python3 examples/10_jog_motion/main.py --model diana7 --ip 192.168.10.75 --mode rotate --duration=0.5 --run
```
