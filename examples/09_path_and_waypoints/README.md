# 09 Path and Waypoints

[English](README.md) | [中文](README.cn.md)

Demonstrates a basic joint path with `createPath`, `addMoveJ`, `runPath`, and `destroyPath`. With `--complex`, it uses `createComplexPath`, `addMoveJByTarget`, `runComplexPath`, and `destroyComplexPath`.

Both modes generate waypoints from the current robot position and then return to the starting joint angles. The first waypoint is J1 +10 degrees for the basic path and J1 +15 degrees for the complex path.

Default mode only prints the two waypoints:

```bash
python3 examples/09_path_and_waypoints/main.py --model diana7 --ip 192.168.10.75
```

Real execution requires `--run`:

```bash
python3 examples/09_path_and_waypoints/main.py --model diana7 --ip 192.168.10.75 --run
python3 examples/09_path_and_waypoints/main.py --model diana7 --ip 192.168.10.75 --complex --run
```

Read [`docs/11_safety.md`](../../docs/11_safety.md) and [`docs/10_path_and_waypoints.md`](../../docs/10_path_and_waypoints.md) before running.
