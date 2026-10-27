# 05 Kinematics

[English](README.md) | [中文](README.cn.md)

演示 `forward`、`inverse`、`inverse_ext`、`rpy2Axis`、`axis2RPY`。`inverse_ext` 以当前关节角为参考，在多解场景中优先选择接近当前姿态的解。关节数组预留 7 个元素，但只按 `getJointCount()` 返回的实际轴数打印。

```bash
python3 examples/05_kinematics/main.py --model diana7 --ip 192.168.10.75
python3 examples/05_kinematics/main.py --model thor12 --ip 192.168.10.75
```

相关教程：[`docs/04_coordinate_pose_and_rotation.cn.md`](../../docs/04_coordinate_pose_and_rotation.cn.md)。
