# 12 ServoL Realtime

[English](README.md) | [中文](README.cn.md)

Demonstrates periodic `servoL_ex` commands. The default is dry-run. During execution, the robot follows a sine trajectory around the current TCP along the base-frame Z direction with +/-5 cm amplitude, for a total travel range of 10 cm. Orientation remains unchanged.

The trajectory runs for 20 seconds with 2000 cycles at 10 ms per cycle, and returns to the starting point instead of continuously moving in one direction. Standard Linux does not guarantee hard realtime behavior, so this example should not be used directly as a production realtime controller.

```bash
# Dry-run: read the current TCP and print the sine-trajectory description, without sending motion commands.
python3 examples/12_servoL_realtime/main.py --model diana7 --ip 192.168.10.75

# Real execution: oscillate around the current TCP along base-frame Z for 20 seconds.
python3 examples/12_servoL_realtime/main.py --model diana7 --ip 192.168.10.75 --run
```
