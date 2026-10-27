# 04 坐标系、位姿与旋转

客户最容易混淆的是“基坐标系中的目标位姿”和“沿工具自身方向移动”。

## 常见坐标概念

- Base：机器人基坐标系
- Flange：末端法兰坐标系
- TCP / Tool：工具中心点坐标系
- Workpiece：工件坐标系（项目使用时）

## `moveLToPose`

目标 `pose[6]` 是基坐标系下的目标 TCP 位姿：

```text
[x, y, z, rx, ry, rz]
```

其中位置单位为 m，旋转采用轴角向量，单位为 rad。

## 为什么“Z + 10 mm”不一定等于“沿工具 Z 走 10 mm”

如果直接修改：

```python
pose[2] += 0.01;
```

表示基坐标系 Z 方向增加 10 mm。

如果客户需要“沿当前 TCP 自身坐标轴移动”，应查看 `moveTCP` / `speedLOnTcp` 等工具坐标系相关接口，而不是简单修改基坐标系 pose。

## 对应例程

- [`04_cartesian_motion`](../examples/04_cartesian_motion/README.cn.md)
- 后续可增加专门的 TCP motion 示例。

## 轴角与 RPY

Diana API 位姿中的 `[rx, ry, rz]` 是单位为 rad 的轴角旋转向量，不是直接的 Roll/Pitch/Yaw。Python wrapper 中的 `rpy2Axis(arr)` 和 `axis2RPY(arr)` 都会原地修改列表；把 RPY 直接传给 `moveLToPose` 会导致错误姿态。

相关例程：[`05_kinematics`](../examples/05_kinematics/README.cn.md)、[`07_tcp_and_frames`](../examples/07_tcp_and_frames/README.cn.md)。
