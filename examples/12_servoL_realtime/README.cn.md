# 12 ServoL Realtime

[English](README.md) | [中文](README.cn.md)

`servoL_ex` 周期下发示例。默认 dry-run；运行时以当前 TCP 为中心，在基坐标系 Z 方向按 ±5 cm 正弦轨迹往复运动（总行程 10 cm），姿态保持不变。轨迹持续 20 秒（2000 个 10 ms 周期）并回到起点，不会持续朝单侧移动。普通 Linux 不保证硬实时，不能直接作为生产实时控制器。

```bash
# 默认只读取当前 TCP 并显示正弦轨迹说明，不发送运动命令
python3 examples/12_servoL_realtime/main.py --model diana7 --ip 192.168.10.75

# 实际执行：围绕当前 TCP 在基坐标系 Z 方向 ±5 cm 往复 20 秒
python3 examples/12_servoL_realtime/main.py --model diana7 --ip 192.168.10.75 --run
```
