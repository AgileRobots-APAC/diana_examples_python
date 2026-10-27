# 01 Getting Started

## Goal

Complete the shortest path from cloning the repository to reading robot state.

## Step 1: Prepare The Robot And PC

- Power on the robot controller normally.
- Connect the PC to the controller API network port by Ethernet.
- Configure the PC and robot in the same subnet.
- Before any motion test, make sure the emergency stop is reachable and the workspace is clear.

## Step 2: Check Network

Assume the robot IP is:

```text
192.168.10.75
```

The PC can use:

```text
192.168.10.100
255.255.255.0
```

Test:

```bash
ping 192.168.10.75
```

## Step 3: Prepare SDK

Clone with the Diana Python SDK submodule:

```bash
git clone --recurse-submodules <your-repo-url>
```

If the repository is already cloned:

```bash
git submodule update --init --recursive
```

## Step 4: Prepare Python Runtime

```bash
export PYTHONPATH="$PWD/third_party/diana_sdk_python/lib:$PYTHONPATH"
export LD_LIBRARY_PATH="$PWD/third_party/diana_sdk_python/lib:$LD_LIBRARY_PATH"
```

For a no-robot check:

```bash
python3 examples/01_connection/main.py --list-models
```

## Step 5: Connect

```bash
python3 examples/01_connection/main.py --ip 192.168.10.75
```

## Step 6: Read State

```bash
python3 examples/02_robot_state/main.py --ip 192.168.10.75
```

If joint angles, TCP pose, and robot state are printed, the basic API communication path is working.

## Next Steps

- Learn non-motion math APIs: `05_kinematics`
- Learn joint motion: `03_joint_motion`
- Learn Cartesian motion: `04_cartesian_motion`

## Select Robot Model

Explicit `--model` is recommended. See [02 Robot models and connection](02_robot_models_and_connection.md).

```bash
python3 examples/01_connection/main.py --list-models
python3 examples/01_connection/main.py --model diana7 --ip 192.168.10.75
python3 examples/01_connection/main.py --model thor12 --ip 192.168.10.75
```
