# 04 Frames, Poses, And Rotations

Users often confuse a target pose in the base frame with motion along the tool's own axes.

## Common Frames

- Base: robot base frame
- Flange: end flange frame
- TCP / Tool: tool center point frame
- Workpiece: workpiece frame

## `moveLToPose`

The target `pose[6]` is a TCP pose in the base frame:

```text
[x, y, z, rx, ry, rz]
```

Position is in meters. Rotation is an axis-angle vector in radians.

## Base Z Is Not Tool Z

Changing:

```python
pose[2] += 0.01
```

moves 10 mm along base-frame Z. To move along the current TCP frame, use tool-frame motion APIs or perform a pose transform first.

## Axis-Angle And RPY

`[rx, ry, rz]` is an axis-angle vector, not Roll/Pitch/Yaw. The Python wrapper functions `rpy2Axis(arr)` and `axis2RPY(arr)` modify the list in place. Passing RPY directly to `moveLToPose` can produce the wrong orientation.

Related examples: [`05_kinematics`](../examples/05_kinematics/README.md), [`07_tcp_and_frames`](../examples/07_tcp_and_frames/README.md).
