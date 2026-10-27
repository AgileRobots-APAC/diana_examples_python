# 02 机器人型号与连接

Diana API 面向多个机器人型号。当前示例仓库把“功能例程”和“机器人型号”分开：

- `examples/`：连接、状态、MoveJ、MoveL、运动学、IO 等通用功能。
- `robots/`：Diana3、Diana7、Diana7 G2、Thor7、Thor12、Thor20 的已注册型号 profile。

## 1. 轴数差异

当前资料中的统一约定：

```text
Diana 系列：7 轴
Thor 系列 ：6 轴
```

所有型号使用同一套 Diana API。连接后可调用：

```python
joint_count = api.getJointCount(ip)
```

用于获取当前机器人轴数。

## 2. 为什么仍然需要 --model

仅凭 6/7 轴不能区分具体型号。例如 7 轴只能说明属于 Diana 系列，不能区分 Diana3、Diana7、Diana7 G2；6 轴同样不能区分 Thor7、Thor12 等。

因此 Python 示例采用显式选择：

```bash
python3 examples/02_robot_state/main.py --model diana7 --ip 192.168.10.75
python3 examples/02_robot_state/main.py --model thor12 --ip 192.168.10.75
```

程序会再用 `getJointCount()` 做轴数校验，避免把 Thor 型号配置用于 7 轴 Diana，或反过来。

## 3. 查看支持型号

```bash
python3 examples/01_connection/main.py --list-models
```

当前支持 key：

```text
diana3
diana7
diana7-g2
thor7
thor12
thor20
```

Thor7 Pro profile 目前暂时未注册，因此不能使用 `--model thor7-pro`。

## 4. 后续型号差异放哪里

如果以后确认某型号有独立的推荐示例姿态、速度限制、构型说明等，只修改：

```text
robots/registry.py
```

不要复制整个 `examples/`，这样所有示例的 API 调用方式仍只维护一份。

## 5. 连接生命周期

连接例程会初始化网络信息、设置机器人 IP、建立 SDK 连接并注册错误/状态回调。回调可能来自后台线程，因此不要在回调中执行长时间阻塞操作。

实际运动时的典型生命周期是：

```text
initSrv → 读取状态 / 控制 → stop（需要时）→ holdBrake（需要时）→ destroySrv
```

`releaseBrake()` 会启动机械臂；调用后应等待约两秒再发送运动指令。`01_connection` 默认不自动上使能，只有显式传入 `--enable` 才会请求该操作。
