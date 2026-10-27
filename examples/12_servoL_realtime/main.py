#!/usr/bin/env python3
# Copyright (c) 2026 Agile Robots SE
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import add_common_arguments, destroy_robot, detect_and_validate_robot, init_robot, print_pose, require_model_for_run, resolve_robot_profile
from robots import print_supported_robot_models

SERVO_PERIOD_SECONDS = 0.01
SERVO_DURATION_SECONDS = 20
SERVO_CYCLE_COUNT = int(SERVO_DURATION_SECONDS / SERVO_PERIOD_SECONDS)
Z_AMPLITUDE_METERS = 0.05


def main() -> int:
    parser = argparse.ArgumentParser(description="Periodic servoL_ex realtime command example.")
    add_common_arguments(parser)
    parser.add_argument("--run", action="store_true", help="Execute the servo trajectory.")
    args = parser.parse_args()
    if args.list_models:
        print_supported_robot_models()
        return 0
    profile = resolve_robot_profile(args)
    require_model_for_run(args, profile)
    api = init_robot(args.ip)
    try:
        detect_and_validate_robot(api, args.ip, profile)
        start_pose = [0.0] * 6
        if not api.getTcpPos(start_pose, args.ip):
            return 5
        print("Start TCP pose:")
        print_pose(start_pose)
        print(f"Servo trajectory: base Z sine wave centered at current TCP, +/-{Z_AMPLITUDE_METERS} m for {SERVO_DURATION_SECONDS} s.")
        if not args.run:
            print("DRY RUN")
            return 0
        if not api.releaseBrake(args.ip):
            return 6
        time.sleep(2)
        ret = True
        for i in range(SERVO_CYCLE_COUNT):
            phase = 2.0 * math.pi * i / (SERVO_CYCLE_COUNT - 1)
            target_pose = start_pose[:]
            target_pose[2] = start_pose[2] + Z_AMPLITUDE_METERS * math.sin(phase)
            ret = api.servoL_ex(target_pose, SERVO_PERIOD_SECONDS, SERVO_PERIOD_SECONDS, 2000, 1.0, False, args.ip)
            if not ret:
                break
            time.sleep(SERVO_PERIOD_SECONDS)
        api.stop(args.ip)
        api.holdBrake(args.ip)
        return 0 if ret else 7
    finally:
        destroy_robot(api, args.ip)


if __name__ == "__main__":
    raise SystemExit(main())
