# 03 Joint Motion

[English](README.md) | [中文](README.cn.md)

Demonstrates `moveJToTarget`. The target is generated from the robot's current joint position by adding 10 degrees to J1, so the example does not assume that different robot models share the same home posture.

Default dry-run:

```bash
python3 examples/03_joint_motion/main.py --model diana7 --ip 192.168.10.75
```

Real motion requires both an explicit model and `--run`:

```bash
python3 examples/03_joint_motion/main.py --model diana7 --ip 192.168.10.75 --run
python3 examples/03_joint_motion/main.py --model thor12 --ip 192.168.10.75 --run
```

The program validates the joint count with `getJointCount()` before motion. Read [`docs/11_safety.md`](../../docs/11_safety.md) before running.
