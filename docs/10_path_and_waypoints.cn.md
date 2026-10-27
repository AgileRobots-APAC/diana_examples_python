# 10 路径与路点

`09_path_and_waypoints` 默认使用 `createPath`、`addMoveJ`、`runPath` 和 `destroyPath` 构造连续关节路径。第一个路点为当前位置的 J1 +10°。传入 `--complex` 时，改用 `createComplexPath`、`addMoveJByTarget`、`runComplexPath` 和 `destroyComplexPath`，第一个路点为 J1 +15°。示例默认 dry-run；实际运行前须核对轨迹、速度、负载和现场净空。
