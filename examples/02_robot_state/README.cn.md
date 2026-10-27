# 02 Robot State

[English](README.md) | [中文](README.cn.md)

读取关节位置、速度、电流、力矩、TCP 位姿、外力和机器人状态，并输出链路、最近错误/警告、碰撞标志和各关节外力/力矩。数组长度不再写死为 6/7，而是连接后通过 `getJointCount()` 确定有效轴数。此例程只读，不会改变机器人状态。

```bash
python3 examples/02_robot_state/main.py --model diana7 --ip 192.168.10.75
python3 examples/02_robot_state/main.py --model thor12 --ip 192.168.10.75
```

相关教程：[`docs/03_robot_state_and_diagnostics.cn.md`](../../docs/03_robot_state_and_diagnostics.cn.md)。
