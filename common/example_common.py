# Copyright (c) 2026 Agile Robots SE
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import importlib
import os
import sys
import time
from pathlib import Path
from typing import Any

from robots import (
    MAX_SUPPORTED_JOINT_COUNT,
    RobotProfile,
    find_robot_profile,
    print_supported_robot_models,
    robot_family_name_from_joint_count,
)


DEFAULT_ROBOT_IP = "192.168.10.75"
_ROOT = Path(__file__).resolve().parents[1]
_DEFAULT_SDK_DIR = _ROOT / "third_party" / "diana_sdk_python"
# Set DIANA_SDK_DIR to use an SDK that is not in third_party/.
_SDK_LIB_DIR = Path(os.environ.get("DIANA_SDK_DIR", _DEFAULT_SDK_DIR)).expanduser() / "lib"
_ERROR_CALLBACK: Any | None = None
_STATE_CALLBACK: Any | None = None


def add_common_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--ip", default=DEFAULT_ROBOT_IP, help="Robot controller IP address.")
    parser.add_argument("--model", help="Robot model key, for example diana7 or thor12.")
    parser.add_argument("--list-models", action="store_true", help="List supported robot models and exit.")


def get_diana_api() -> Any:
    sdk_path = str(_SDK_LIB_DIR)
    if sdk_path not in sys.path:
        sys.path.insert(0, sdk_path)
    return importlib.import_module("DianaApi")


def resolve_robot_profile(args: argparse.Namespace) -> RobotProfile | None:
    profile = find_robot_profile(getattr(args, "model", None))
    if getattr(args, "model", None) and profile is None:
        print(f"Unknown robot model: {args.model}", file=sys.stderr)
        print_supported_robot_models()
        raise SystemExit(1)
    return profile


def require_model_for_run(args: argparse.Namespace, profile: RobotProfile | None) -> None:
    if getattr(args, "run", False) and profile is None:
        print("For safety, --run requires an explicit --model.", file=sys.stderr)
        raise SystemExit(2)


def _error_callback(error_code: int, ip: bytes | None) -> None:
    api = get_diana_api()
    ip_text = ip.decode("utf-8") if ip else ""
    try:
        message = api.formatError(error_code, ip_text)
    except Exception:
        message = None
    print(
        f"[Diana API error] code={error_code} ip={ip_text} message={message or 'unknown'}",
        file=sys.stderr,
    )


def _state_callback(_state: Any, _ip: bytes | None) -> None:
    # Keep callbacks non-blocking; examples query cached state explicitly.
    return None


def init_robot(ip: str) -> Any:
    global _ERROR_CALLBACK, _STATE_CALLBACK

    api = get_diana_api()
    _ERROR_CALLBACK = api.FNCERRORCALLBACK(_error_callback)
    _STATE_CALLBACK = api.FNCSTATECALLBACK(_state_callback)
    ok = api.initSrv([ip, 0, 0, 0, 0, 0], _ERROR_CALLBACK, _STATE_CALLBACK)
    if not ok:
        print(f"initSrv failed, ip={ip}", file=sys.stderr)
        raise SystemExit(2)
    time.sleep(0.2)
    return api


def destroy_robot(api: Any, ip: str) -> None:
    try:
        api.destroySrv(ip)
    except Exception as exc:
        print(f"destroySrv failed: {exc}", file=sys.stderr)


def detect_and_validate_robot(api: Any, ip: str, profile: RobotProfile | None) -> int:
    joint_count = int(api.getJointCount(ip))
    if joint_count <= 0 or joint_count > MAX_SUPPORTED_JOINT_COUNT:
        print(f"getJointCount failed or returned unsupported count: {joint_count}", file=sys.stderr)
        raise SystemExit(3)

    print(f"Detected joint count: {joint_count} ({robot_family_name_from_joint_count(joint_count)})")
    if profile is None:
        print("Exact model: not selected. Use --model <name> to select and validate it.")
        return joint_count

    print(f"Selected model: {profile.display_name} (expected {profile.joint_count} axes)")
    if joint_count != profile.joint_count:
        print(
            "Robot model mismatch: selected "
            f"{profile.display_name} expects {profile.joint_count} axes, "
            f"but the connected robot reports {joint_count}.",
            file=sys.stderr,
        )
        raise SystemExit(4)
    return joint_count


def wait_move(api: Any, ip: str) -> None:
    time.sleep(0.2)
    while api.getRobotState(ip) == 0:
        time.sleep(0.01)


def print_joints(joints: list[float], count: int) -> None:
    for index in range(count):
        print(f"  J{index + 1}: {joints[index]:.6f} rad")


def print_pose(pose: list[float]) -> None:
    labels = ("x ", "y ", "z ", "rx", "ry", "rz")
    units = ("m", "m", "m", "rad", "rad", "rad")
    for label, value, unit in zip(labels, pose, units):
        print(f"  {label}: {value:.6f} {unit}")


def print_wrench(wrench: list[float]) -> None:
    labels = ("Fx", "Fy", "Fz", "Tx", "Ty", "Tz")
    units = ("N", "N", "N", "Nm", "Nm", "Nm")
    for label, value, unit in zip(labels, wrench, units):
        print(f"  {label}: {value:.6f} {unit}")


def robot_state_name(state: int) -> str:
    names = {
        0: "running",
        1: "paused",
        2: "idle",
        3: "free-driving",
        4: "zero-space-free-driving",
        5: "hold-brake",
        6: "error",
        7: "handling-error",
        8: "rescue-mode",
    }
    return names.get(int(state), "unknown")
