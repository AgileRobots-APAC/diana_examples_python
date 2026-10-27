# 08 Motion Limits

[English](README.md) | [中文](README.cn.md)

Read-only example that prints the controller's current joint position, velocity, and acceleration limits, plus Cartesian translation / rotation velocity and acceleration limits.

```bash
python3 examples/08_motion_limits/main.py --model thor12 --ip 192.168.10.75
```

This example does not call any `set*Limit` API.

Related documentation: [`docs/09_motion_limits.md`](../../docs/09_motion_limits.md).
