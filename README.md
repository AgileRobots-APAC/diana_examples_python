# Diana API Python Examples

[English](README.md) | [中文](README.cn.md)

Python examples and learning notes for **Diana / Thor series robots** using the official Diana Python SDK.

This repository is intended to help users clone the project, provide the official SDK, choose a robot model, pass the robot IP address, and learn the common API workflow from connection and state reading through motion, I/O, frames, payloads, paths, and realtime commands.

> This project does not wrap or replace the official robot SDK. The programs in `examples/` call the original Diana Python API directly where possible. The `common/` directory only contains shared helpers for argument parsing, callbacks, waiting, printing, SDK loading, and robot model validation.

## Supported Models

```text
Diana series (7 axes)
├── Diana3       -> --model diana3
├── Diana7       -> --model diana7
└── Diana7 G2    -> --model diana7-g2

Thor series (6 axes)
├── Thor7        -> --model thor7
├── Thor12       -> --model thor12
└── Thor20       -> --model thor20
```

All models share the same examples. Model-specific data is kept in [`robots/`](robots/), and each connection can be checked with `getJointCount()` to validate Diana 7-axis robots and Thor 6-axis robots.

## Navigation

- [Documentation index](docs/README.md)
- [Python smoke test notes](docs/platform_compatibility_test.md)
- [01 Connection and model validation](examples/01_connection/README.md)
- [02 Robot state and diagnostics](examples/02_robot_state/README.md)
- [03 Joint motion](examples/03_joint_motion/README.md)
- [04 Cartesian motion](examples/04_cartesian_motion/README.md)
- [05 Kinematics](examples/05_kinematics/README.md)
- [06 I/O](examples/06_io/README.md)
- [07 TCP, frames, and payload](examples/07_tcp_and_frames/README.md)
- [08 Motion limits](examples/08_motion_limits/README.md)
- [09 Paths and waypoints](examples/09_path_and_waypoints/README.md)
- [10 Jog motion](examples/10_jog_motion/README.md)
- [11 Force guarded motion](examples/11_force_guarded_motion/README.md)
- [12 Realtime ServoL](examples/12_servoL_realtime/README.md)

## Repository Layout

| Path | Description |
|---|---|
| [`examples/`](examples/) | Runnable Python examples. Motion examples are dry-run by default unless `--run` is specified. |
| [`common/`](common/) | Shared helper code for examples. |
| [`robots/`](robots/) | Robot model profiles and registry. |
| [`docs/`](docs/) | Learning notes, safety notes, FAQ, and compatibility checks. |
| [`third_party/diana_sdk_python/`](third_party/diana_sdk_python/) | Official DianaApi Python SDK submodule location. |

## SDK Setup

Clone with submodules enabled:

```bash
git clone --recurse-submodules <your-repo-url>
cd diana-api-examples-python
```

If the main repository has already been cloned, initialize the submodule with:

```bash
git submodule update --init --recursive
```

The submodule includes the SDK 3.3.0 native runtime for Linux x86_64. Set the Python wrapper and native library search paths before running an example:

```bash
export PYTHONPATH="$PWD/third_party/diana_sdk_python/lib:$PYTHONPATH"
export LD_LIBRARY_PATH="$PWD/third_party/diana_sdk_python/lib:$LD_LIBRARY_PATH"
```

To use an SDK that is not in `third_party/`, set `DIANA_SDK_DIR` to its directory (the one that contains `lib/`) and point `PYTHONPATH` and `LD_LIBRARY_PATH` at its `lib/` directory instead:

```bash
export DIANA_SDK_DIR=/path/to/diana_sdk_python
export PYTHONPATH="$DIANA_SDK_DIR/lib:$PYTHONPATH"
export LD_LIBRARY_PATH="$DIANA_SDK_DIR/lib:$LD_LIBRARY_PATH"
```

## First Run

List supported models without loading the native SDK:

```bash
python3 examples/01_connection/main.py --list-models
```

Connect to a Diana7:

```bash
python3 examples/01_connection/main.py --model diana7 --ip 192.168.10.75
```

Connect to a Thor12:

```bash
python3 examples/01_connection/main.py --model thor12 --ip 192.168.10.75
```

Before connecting, make sure the PC and robot are on the same network segment:

```bash
ping 192.168.10.75
```

## Safety

Motion examples calculate and print their targets by default. They do not send motion commands unless `--run` is specified.

Real motion requires an explicit robot model:

```bash
python3 examples/03_joint_motion/main.py --model diana7 --ip 192.168.10.75 --run
python3 examples/04_cartesian_motion/main.py --model thor12 --ip 192.168.10.75 --run
```

The examples also call `getJointCount()` after connecting to validate the model family. Read [`docs/11_safety.md`](docs/11_safety.md) before running motion examples.

## Smoke Tests

Run the repository checks without connecting to a robot:

```bash
python3 scripts/check_repository.py
```

The script checks Python syntax, SDK method references, local Markdown links, bilingual document pairs, and every example's `--list-models` path. It does not validate robot communication or motion.

## Documentation Basis

The examples and tutorials are based on the Diana industrial robot API manual for Python and the Diana controller interface documentation. Always use the official API manual that matches the SDK version installed at the customer site as the final reference.


## Compatibility

| Examples version | SDK version | SDK `version` file |
|---|---|---|
| 1.0.0 | 3.3.0 | `industry-v3.3.0.260211` |

The SDK submodule is pinned to the SDK tag listed above. To use another SDK version, see "SDK Setup" and verify the examples against it before use.

## License

The example source in this repository is licensed under the MIT License; see [`LICENSE`](LICENSE). The Diana SDK referenced as a submodule is a separate repository and is not covered by this license.
