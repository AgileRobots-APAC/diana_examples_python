# 03 Joint Motion

[English](README.md) | [中文](README.cn.md)

演示 `moveJToTarget`。目标基于机器人当前关节位置，只对 J1 增加 10°，不假设不同型号共用同一 Home 姿态。

默认 dry-run：

```bash
python3 examples/03_joint_motion/main.py --model diana7 --ip 192.168.10.75
```

真正运动必须同时指定具体型号和 `--run`：

```bash
python3 examples/03_joint_motion/main.py --model diana7 --ip 192.168.10.75 --run
python3 examples/03_joint_motion/main.py --model thor12 --ip 192.168.10.75 --run
```

程序会先用 `getJointCount()` 校验轴数。运行前阅读 [`docs/11_safety.cn.md`](../../docs/11_safety.cn.md)。
