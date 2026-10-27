# 10 Jog Motion

[English](README.md) | [中文](README.cn.md)

Low-speed jog example. The default mode jogs J1 in the positive direction. Use `--mode` to select two additional TCP jog modes:

- `--mode joint`: jog J1 in the positive direction, the default mode.
- `--mode tcp`: call `moveTcp_ex` and translate along the base-frame +X direction.
- `--mode rotate`: call `rotationTCP` and rotate around the base-frame +Z axis.

The default is dry-run. Execution requires `--model ... --run`, and `--duration=0.1..2.0` can be used to limit the duration. The program always calls `stop()` and `holdBrake()`.

```bash
python3 examples/10_jog_motion/main.py --model diana7 --ip 192.168.10.75
python3 examples/10_jog_motion/main.py --model diana7 --ip 192.168.10.75 --mode joint --duration=0.5 --run
python3 examples/10_jog_motion/main.py --model diana7 --ip 192.168.10.75 --mode tcp --duration=0.5 --run
python3 examples/10_jog_motion/main.py --model diana7 --ip 192.168.10.75 --mode rotate --duration=0.5 --run
```
