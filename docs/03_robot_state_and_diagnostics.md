# 03 Robot State, Errors, And Diagnostics

## Error Callback

`initSrv` registers an error callback. The examples format error codes with:

```python
api.formatError(error_code, ip)
```

## API Return Values

Many common APIs use:

```text
0      success at the native layer
< 0    failure at the native layer
```

The Python wrapper often converts this into `True` / `False`. Do not assume a motion or write completed after a failed call.

## Common Motion Errors

Controller documentation lists errors such as:

- IK singularity
- IK joint position limit
- IK failure
- Joint planning failure
- Cartesian speed limit
- Torque limit

Interpret them together with `formatError`, robot state, and teach pendant alarms.

## Callback Notes

Callbacks may run in background SDK threads:

- Do not sleep for a long time.
- Do not perform blocking I/O.
- Only record, flag, or notify quickly.

## Diagnostics

`02_robot_state` reads joints, TCP pose, velocities, currents, torques, link state, latest error/warning, collision flag, TCP wrench, and joint force/torque. It is read-only.
