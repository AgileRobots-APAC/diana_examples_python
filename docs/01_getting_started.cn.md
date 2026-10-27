# 01 快速开始

## 目标

完成从“拿到仓库”到“成功读取机器人状态”的最短路径。

## 步骤 1：准备机器人与 PC

- 机器人控制箱正常上电。
- PC 使用以太网连接控制箱 API 网络口。
- PC 与机器人配置到同一子网。
- 运动测试时确保急停可触及、工作空间无人且无障碍物。

## 步骤 2：确认网络

假设机器人 IP 为：

```text
192.168.10.75
```

PC 可以设置为：

```text
192.168.10.100
255.255.255.0
```

测试：

```bash
ping 192.168.10.75
```

## 步骤 3：准备 SDK

首次克隆时，使用 Git submodule 一并获取官方 Diana Python SDK：

```bash
git clone --recurse-submodules <your-repo-url>
```

SDK 位于：

```text
third_party/diana_sdk_python/
```

如果已经克隆主仓库，再执行：

```bash
git submodule update --init --recursive
```

## 步骤 4：准备 Python 运行环境

```bash
export PYTHONPATH="$PWD/third_party/diana_sdk_python/lib:$PYTHONPATH"
export LD_LIBRARY_PATH="$PWD/third_party/diana_sdk_python/lib:$LD_LIBRARY_PATH"
```

如果只想先做不连接机器人的检查，可运行：

```bash
python3 examples/01_connection/main.py --list-models
```

SDK 的目录结构、依赖库和版本替换规则见 [`third_party/diana_sdk_python/README.md`](../third_party/diana_sdk_python/README.md)。

## 步骤 5：连接

```bash
python3 examples/01_connection/main.py --ip 192.168.10.75
```

## 步骤 6：读取状态

```bash
python3 examples/02_robot_state/main.py --ip 192.168.10.75
```

如果能看到关节角、TCP 位姿和机器人状态，最基础的 API 通信已经打通。

## 下一步

- 不运动学习数学接口：`05_kinematics`
- 学习关节运动：`03_joint_motion`
- 学习直线运动：`04_cartesian_motion`


## 选择机器人型号

推荐显式使用 `--model`。详细说明见 [02_robot_models_and_connection.md](02_robot_models_and_connection.cn.md)。

```bash
python3 examples/01_connection/main.py --list-models
python3 examples/01_connection/main.py --model diana7 --ip 192.168.10.75
python3 examples/01_connection/main.py --model thor12 --ip 192.168.10.75
```
