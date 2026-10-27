# 05 关节运动

## 到一个目标点，不强调 TCP 路径

优先考虑关节空间运动：

```text
moveJToTarget / moveJToPose / moveJ
```

本仓库例程：`03_joint_motion`

## 型号选择

真正发送运动命令时，示例要求显式传入 `--model`，并使用 `getJointCount()` 校验轴数。例如：

```bash
python3 examples/03_joint_motion/main.py --model diana7 --ip 192.168.10.75 --run
python3 examples/03_joint_motion/main.py --model thor12 --ip 192.168.10.75 --run
```
