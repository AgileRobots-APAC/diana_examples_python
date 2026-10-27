# 07 TCP and Frames

[English](README.md) | [中文](README.cn.md)

只读显示当前 TCP 位姿、默认活动 TCP 相对法兰的位姿与齐次矩阵、默认 TCP/工件坐标系名称及活动 TCP 负载参数。还会把工具坐标系下的偏移换算为基坐标系目标位姿。

SDK 的默认 TCP 和工件坐标系名称查询需要调用方提供 256 字节缓冲区；示例已按此要求分配，避免名称查询损坏栈内存。

```bash
python3 examples/07_tcp_and_frames/main.py --model diana7 --ip 192.168.10.75
python3 examples/07_tcp_and_frames/main.py --model diana7 --ip 192.168.10.75 --offset=0,0,0.01,0,0,0
```

`--offset` 格式为 `x,y,z,roll,pitch,yaw`，位置单位为米，角度单位为度。不会修改 TCP、负载或工件坐标系。相关教程：[`docs/08_tcp_frames_and_payload.cn.md`](../../docs/08_tcp_frames_and_payload.cn.md)。
