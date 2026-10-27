# 02 Robot Models And Connection

Diana API supports multiple robot models. This repository separates feature examples from robot model profiles:

- `examples/`: connection, state, MoveJ, MoveL, kinematics, I/O, and other common workflows.
- `robots/`: registered profiles for Diana3, Diana7, Diana7 G2, Thor7, Thor12, and Thor20.

## Joint Count

Current convention:

```text
Diana series: 7 axes
Thor series : 6 axes
```

After connecting, call:

```python
joint_count = api.getJointCount(ip)
```

## Why `--model` Is Still Needed

Joint count only identifies the family. Seven axes cannot distinguish Diana3, Diana7, and Diana7 G2; six axes cannot distinguish Thor7, Thor12, and Thor20.

The examples therefore support explicit model selection:

```bash
python3 examples/02_robot_state/main.py --model diana7 --ip 192.168.10.75
python3 examples/02_robot_state/main.py --model thor12 --ip 192.168.10.75
```

The program then validates the connected robot with `getJointCount()`.

## Supported Keys

```bash
python3 examples/01_connection/main.py --list-models
```

```text
diana3
diana7
diana7-g2
thor7
thor12
thor20
```

Thor7 Pro is not registered yet, so `--model thor7-pro` is unavailable.

## Where Model Differences Live

If a model later needs dedicated recommended poses, speed limits, or configuration notes, update `robots/registry.py`. Do not duplicate the whole `examples/` tree.

## Connection Lifecycle

Typical lifecycle:

```text
initSrv -> read state / control -> stop when needed -> holdBrake when needed -> destroySrv
```

Callbacks may run from SDK background threads; keep them short and non-blocking. After `releaseBrake()`, wait about two seconds before sending motion commands.
