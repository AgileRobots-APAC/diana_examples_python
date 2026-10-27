# Python Smoke Tests

This repository provides lightweight smoke tests for Python syntax, common CLI options, and the no-robot `--list-models` path.

## Checks

| Check | Command | Connects to robot |
|---|---|---|
| Python syntax | `python3 -m py_compile common/*.py robots/*.py examples/*/main.py` | No |
| Model-list CLI | `for f in examples/*/main.py; do python3 "$f" --list-models >/dev/null; done` | No |

`--list-models` exits before importing the native DianaApi library, so it can run without a robot and without the native runtime library.

## Local Smoke Test

```bash
git submodule update --init --recursive
python3 -m py_compile common/*.py robots/*.py examples/*/main.py
for f in examples/*/main.py; do python3 "$f" --list-models >/dev/null; done
```

These checks do not cover robot communication or motion.

## Real Robot Validation

On a target machine, set SDK paths:

```bash
export PYTHONPATH="$PWD/third_party/diana_sdk_python/lib:$PYTHONPATH"
export LD_LIBRARY_PATH="$PWD/third_party/diana_sdk_python/lib:$LD_LIBRARY_PATH"
```

Then run:

```bash
python3 examples/01_connection/main.py --model diana7 --ip <robot-ip>
python3 examples/02_robot_state/main.py --model diana7 --ip <robot-ip>
```

Validate dry-run examples next. Any `--run` test must be performed manually after checking people, speed, payload, clearance, and emergency stop access.
