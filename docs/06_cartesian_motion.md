# 06 Cartesian Motion

Use Cartesian motion when the TCP must move linearly to a target pose. Common APIs include `moveLToPose`, `moveLToTarget`, and `moveL`.

`04_cartesian_motion` reads the current TCP pose, adds 10 mm along base-frame Z, and prints the target by default. It sends motion only with `--model ... --run`.

Check TCP, payload, velocity, clearance, and singularity risk before running. Moving along the tool frame is different from moving along the base frame; see [08 TCP, frames, and payload](08_tcp_frames_and_payload.md).
