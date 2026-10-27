# 10 Paths And Waypoints

`09_path_and_waypoints` demonstrates basic joint paths with `createPath`, `addMoveJ`, `runPath`, and `destroyPath`.

With `--complex`, it uses the complex path APIs. Both modes generate waypoints from the current joint position and then return to the start. The example is dry-run by default; real execution requires `--model ... --run`.
