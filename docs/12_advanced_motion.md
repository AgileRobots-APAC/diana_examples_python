# 12 Advanced Motion

`10_jog_motion`, `11_force_guarded_motion`, and `12_servoL_realtime` are dry-run by default. Real execution requires explicit `--model` and `--run`.

- Jog: J1 positive jog by default. `--mode tcp` calls `moveTcp_ex` along base +X; `--mode rotate` calls `rotationTCP` around base +Z. The example always calls `stop()` and `holdBrake()`.
- Force guarded motion: moves slowly in Cartesian X and stops when TCP Fx reaches the threshold or timeout.
- ServoL: sends a 10 ms periodic `servoL_ex` command following a +/-5 cm sine trajectory around the current TCP along base Z for 20 seconds.

Standard Linux does not guarantee hard realtime behavior. Do not use the ServoL example directly as a production realtime controller.
