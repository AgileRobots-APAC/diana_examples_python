# 11 Safety

> Motion examples are API references only. Users must evaluate the real robot model, installation, tool, payload, and site risks before running them.

Before first motion:

- Make sure the emergency stop is reachable.
- Keep the robot workspace clear.
- Confirm the tool, TCP, and payload settings.
- Start with low speed and acceleration.
- Do not copy absolute joint angles or poses from another site.

Motion examples are dry-run by default. They connect, read the current state, calculate a small target, and print it without sending motion commands. Add `--model <name> --run` only after checking the workspace.

`releaseBrake()` enables the robot; wait about two seconds before sending motion. `stop()` is not a replacement for the emergency stop.
