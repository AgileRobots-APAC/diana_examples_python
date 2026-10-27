# 06 笛卡尔运动

当 TCP 必须沿直线到达目标时，使用 `moveLToPose`、`moveLToTarget` 或 `moveL`。目标位姿是基坐标系下的 TCP 位姿，位置单位为 m，旋转是轴角向量、单位为 rad。

`04_cartesian_motion` 默认只计算并打印目标；只有指定 `--model` 与 `--run` 才会真正发送运动指令。执行前应确认 TCP、负载、速度、净空和奇异位姿风险。

“沿工具自身坐标轴移动”与“沿基坐标系移动”不同。前者需要工具坐标系相关接口或先进行位姿变换；参见 [08 TCP、坐标系与负载](08_tcp_frames_and_payload.cn.md)。
