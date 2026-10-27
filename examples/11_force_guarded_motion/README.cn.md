# 11 Force Guarded Motion

[English](README.md) | [中文](README.cn.md)

受力阈值停止示例：低速沿基坐标 X 运动，检测到 `|Fx| >= 5 N` 或 10 秒后停止。默认 dry-run；仅可在完成力传感、负载和工作空间评审后使用 `--run`。

```bash
# 默认只显示动作说明，不发送运动命令
python3 examples/11_force_guarded_motion/main.py --model diana7 --ip 192.168.10.75

# 实际执行：低速沿基坐标系 X 方向运动，受力达到阈值或 10 秒后停止
python3 examples/11_force_guarded_motion/main.py --model diana7 --ip 192.168.10.75 --run
```

运行结束时，程序会说明停止原因为力阈值、正常超时或运动指令失败；同时输出触发或最后一次有效采样的 `Fx`，以及 `+/-5 N` 阈值。
