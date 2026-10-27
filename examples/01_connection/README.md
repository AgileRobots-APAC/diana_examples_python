# 01 Connection

[English](README.md) | [中文](README.cn.md)

Demonstrates the Diana API lifecycle: `initSrv`, version and state reads, and `destroySrv`. It also adds robot model selection and `getJointCount()` validation.

```bash
python3 examples/01_connection/main.py --list-models
python3 examples/01_connection/main.py --model diana7 --ip 192.168.10.75
python3 examples/01_connection/main.py --model thor12 --ip 192.168.10.75
```

By default, this example does not call `releaseBrake()`. To explicitly demonstrate enable / disable behavior:

```bash
python3 examples/01_connection/main.py --model diana7 --ip 192.168.10.75 --enable
```

Related documentation: [`docs/02_robot_models_and_connection.md`](../../docs/02_robot_models_and_connection.md).
