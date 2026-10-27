# 02 Robot State

[English](README.md) | [中文](README.cn.md)

Reads joint position, velocity, current, torque, TCP pose, external force, and robot state. It also prints link status, the latest error / warning, collision flags, and external force / torque for each joint.

The valid joint count is determined after connection with `getJointCount()`, so arrays are not hard-coded to 6 or 7 axes. This example is read-only and does not change robot state.

```bash
python3 examples/02_robot_state/main.py --model diana7 --ip 192.168.10.75
python3 examples/02_robot_state/main.py --model thor12 --ip 192.168.10.75
```

Related documentation: [`docs/03_robot_state_and_diagnostics.md`](../../docs/03_robot_state_and_diagnostics.md).
