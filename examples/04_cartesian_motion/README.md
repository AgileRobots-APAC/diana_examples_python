# 04 Cartesian Motion

[English](README.md) | [中文](README.cn.md)

Demonstrates `moveLToPose`. The target is the current TCP pose translated by +10 mm along the base-frame Z axis.

Default dry-run:

```bash
python3 examples/04_cartesian_motion/main.py --model diana7 --ip 192.168.10.75
```

Real motion:

```bash
python3 examples/04_cartesian_motion/main.py --model thor12 --ip 192.168.10.75 --run
```

`--run` must be used together with `--model`, and the program validates the robot joint count before motion. Read [`docs/11_safety.md`](../../docs/11_safety.md) before running.
