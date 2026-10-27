# 11 Force Guarded Motion

[English](README.md) | [中文](README.cn.md)

Force-threshold stop example. The robot moves slowly along the base-frame X direction and stops when `|Fx| >= 5 N` is detected or after 10 seconds. The default is dry-run; use `--run` only after reviewing the force sensor, payload, and workspace.

```bash
# Dry-run: only print the motion description, without sending a motion command.
python3 examples/11_force_guarded_motion/main.py --model diana7 --ip 192.168.10.75

# Real execution: move slowly along base-frame X until the force threshold is reached or 10 seconds elapse.
python3 examples/11_force_guarded_motion/main.py --model diana7 --ip 192.168.10.75 --run
```

At the end of the run, the program reports whether it stopped because of the force threshold, normal timeout, or motion command failure. It also prints the triggered or last valid `Fx` sample and the `+/-5 N` threshold.
