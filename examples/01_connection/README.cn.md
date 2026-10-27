# 01 Connection

[English](README.md) | [中文](README.cn.md)

演示 API 生命周期：`initSrv`、版本/状态读取、`destroySrv`，并增加型号选择和 `getJointCount()` 校验。

```bash
python3 examples/01_connection/main.py --list-models
python3 examples/01_connection/main.py --model diana7 --ip 192.168.10.75
python3 examples/01_connection/main.py --model thor12 --ip 192.168.10.75
```

默认不会调用 `releaseBrake()`。如需专门演示上/下使能：

```bash
python3 examples/01_connection/main.py --model diana7 --ip 192.168.10.75 --enable
```

相关教程：[`docs/02_robot_models_and_connection.cn.md`](../../docs/02_robot_models_and_connection.cn.md)。
