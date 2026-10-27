#!/usr/bin/env python3
# Copyright (c) 2026 Agile Robots SE
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import add_common_arguments, destroy_robot, detect_and_validate_robot, init_robot, print_pose, require_model_for_run, resolve_robot_profile, wait_move
from robots import print_supported_robot_models


def main() -> int:
    parser = argparse.ArgumentParser(description="Cartesian linear motion with moveLToPose.")
    add_common_arguments(parser)
    parser.add_argument("--run", action="store_true", help="Send the motion command.")
    args = parser.parse_args()
    if args.list_models:
        print_supported_robot_models()
        return 0

    profile = resolve_robot_profile(args)
    require_model_for_run(args, profile)
    api = init_robot(args.ip)
    try:
        detect_and_validate_robot(api, args.ip, profile)
        start = [0.0] * 6
        if not api.getTcpPos(start, args.ip):
            return 5
        target = start[:]
        target[2] += 0.01
        print("Current TCP pose:")
        print_pose(start)
        print("Example target (Base Z + 10 mm):")
        print_pose(target)
        if not args.run:
            print("DRY RUN: no motion command sent. Add --model <name> --run after checking the workspace.")
            return 0
        if not api.releaseBrake(args.ip):
            return 6
        time.sleep(2)
        if not api.moveLToPose(target, 0.02, 0.05, 0, 0.0, 0.0, False, args.ip):
            api.stop(args.ip)
            api.holdBrake(args.ip)
            return 7
        wait_move(api, args.ip)
        print("Motion finished.")
        api.holdBrake(args.ip)
    finally:
        destroy_robot(api, args.ip)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
