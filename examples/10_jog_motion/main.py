#!/usr/bin/env python3
# Copyright (c) 2026 Agile Robots SE
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import add_common_arguments, destroy_robot, detect_and_validate_robot, init_robot, require_model_for_run, resolve_robot_profile
from robots import print_supported_robot_models


def main() -> int:
    parser = argparse.ArgumentParser(description="Low-speed jog motion.")
    add_common_arguments(parser)
    parser.add_argument("--run", action="store_true", help="Execute jog motion.")
    parser.add_argument("--mode", choices=("joint", "tcp", "rotate"), default="joint")
    parser.add_argument("--duration", type=float, default=0.5)
    args = parser.parse_args()
    if args.list_models:
        print_supported_robot_models()
        return 0
    profile = resolve_robot_profile(args)
    require_model_for_run(args, profile)
    if args.duration < 0.1 or args.duration > 2.0:
        print("--duration must be 0.1..2.0 seconds", file=sys.stderr)
        return 5
    api = init_robot(args.ip)
    try:
        detect_and_validate_robot(api, args.ip, profile)
        messages = {
            "joint": "Jog J1 positive",
            "tcp": "Jog TCP along base +X",
            "rotate": "Rotate TCP about base +Z",
        }
        print(f"{messages[args.mode]} for {args.duration} s at low speed.")
        if not args.run:
            print("DRY RUN")
            return 0
        if not api.releaseBrake(args.ip):
            return 6
        time.sleep(2)
        if args.mode == "joint":
            ok = api.moveJoint(api.joint_direction_e.T_MOVE_UP, 0, 0.05, 0.10, args.ip)
        elif args.mode == "tcp":
            ok = api.moveTcp_ex(api.coordinate_e.E_BASE_COORDINATE, api.tcp_direction_e.T_MOVE_X_UP, 0.01, 0.02, args.ip)
        else:
            ok = api.rotationTCP(api.tcp_direction_e.T_MOVE_Z_UP, 0.05, 0.10, args.ip)
        time.sleep(args.duration)
        api.stop(args.ip)
        api.holdBrake(args.ip)
        return 0 if ok else 7
    finally:
        destroy_robot(api, args.ip)


if __name__ == "__main__":
    raise SystemExit(main())
