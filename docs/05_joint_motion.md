# 05 Joint Motion

Use joint-space motion when the robot should reach a target joint posture and the TCP path does not need to be a straight line.

The main example is `03_joint_motion`, which reads current joints, adds 10 degrees to J1, prints the target, and only moves when `--run` is present.

Real motion requires an explicit model:

```bash
python3 examples/03_joint_motion/main.py --model diana7 --ip 192.168.10.75 --run
```

The example validates `getJointCount()` before motion.
