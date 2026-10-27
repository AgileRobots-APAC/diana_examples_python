# 07 TCP and Frames

[English](README.md) | [中文](README.cn.md)

Read-only example that prints the current TCP pose, the active default TCP pose relative to the flange, its homogeneous matrix, default TCP / workpiece frame names, and active TCP payload parameters. It also converts a tool-frame offset into a base-frame target pose.

The SDK default TCP and workpiece frame name queries require the caller to provide a 256-byte buffer. This example allocates the required buffer size to avoid stack memory corruption during name queries.

```bash
python3 examples/07_tcp_and_frames/main.py --model diana7 --ip 192.168.10.75
python3 examples/07_tcp_and_frames/main.py --model diana7 --ip 192.168.10.75 --offset=0,0,0.01,0,0,0
```

The `--offset` format is `x,y,z,roll,pitch,yaw`; position is in meters and angles are in degrees. This example does not modify TCP, payload, or workpiece frame settings.

Related documentation: [`docs/08_tcp_frames_and_payload.md`](../../docs/08_tcp_frames_and_payload.md).
