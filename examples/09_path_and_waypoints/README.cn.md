# 09 Path and Waypoints

[English](README.md) | [中文](README.cn.md)

演示基础关节路径 `createPath`、`addMoveJ`、`runPath`、`destroyPath`。传入 `--complex` 时，改用 `createComplexPath`、`addMoveJByTarget`、`runComplexPath`、`destroyComplexPath`。两种模式都基于当前位置生成路点后返回起始关节角：基础路径的第一个路点为 J1 +10°，复杂路径为 J1 +15°。

默认仅打印两个路点：

```bash
python3 examples/09_path_and_waypoints/main.py --model diana7 --ip 192.168.10.75
```

实际执行需明确指定 `--run`：

```bash
python3 examples/09_path_and_waypoints/main.py --model diana7 --ip 192.168.10.75 --run
python3 examples/09_path_and_waypoints/main.py --model diana7 --ip 192.168.10.75 --complex --run
```

运行前阅读 [`docs/11_safety.cn.md`](../../docs/11_safety.cn.md) 和 [`docs/10_path_and_waypoints.cn.md`](../../docs/10_path_and_waypoints.cn.md)。
