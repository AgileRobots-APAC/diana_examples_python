# 12 高级运动

`10_jog_motion`、`11_force_guarded_motion` 和 `12_servoL_realtime` 都默认 dry-run，实际执行必须显式传入 `--model` 和 `--run`。

- 点动：`10_jog_motion` 默认执行低速、短时长 J1 正向运动。`--mode tcp` 调用 `moveTcp_ex` 沿基坐标系 +X 平移，`--mode rotate` 调用 `rotationTCP` 绕基坐标系 +Z 旋转；三种模式完成后总会调用 `stop()` 和 `holdBrake()`。
- 力阈值停止：低速笛卡尔运动中轮询 TCP 外力，达到阈值或超时即停止；应先完成现场力控与碰撞风险评审。
- ServoL：以 10 ms 周期生成围绕当前 TCP 的基坐标系 Z 向 ±5 cm 正弦轨迹（总行程 10 cm），持续 20 秒（2000 次）后回到起点，仅用于理解接口模式。普通 Linux 不保证硬实时，不能直接作为生产级实时控制方案。

执行任何高级运动前，必须遵守 [安全说明](11_safety.cn.md)，并在低速、空载、净空充足的工作空间内验证。
