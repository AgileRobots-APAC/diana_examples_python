#!/usr/bin/env python3
# Copyright (c) 2026 Agile Robots SE
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import add_common_arguments, destroy_robot, detect_and_validate_robot, init_robot, resolve_robot_profile
from robots import MAX_SUPPORTED_JOINT_COUNT, print_supported_robot_models


def main() -> int:
    parser = argparse.ArgumentParser(description="Read controller motion limits.")
    add_common_arguments(parser)
    args = parser.parse_args()
    if args.list_models:
        print_supported_robot_models()
        return 0
    profile = resolve_robot_profile(args)
    api = init_robot(args.ip)
    try:
        count = detect_and_validate_robot(api, args.ip, profile)
        min_pos = [0.0] * MAX_SUPPORTED_JOINT_COUNT
        max_pos = [0.0] * MAX_SUPPORTED_JOINT_COUNT
        max_vel = [0.0] * MAX_SUPPORTED_JOINT_COUNT
        max_acc = [0.0] * MAX_SUPPORTED_JOINT_COUNT
        if api.getJointsPositionRange(min_pos, max_pos, args.ip) and api.getMaxJointsVel(max_vel, args.ip) and api.getMaxJointsAcc(max_acc, args.ip):
            print("Joint limits (rad, rad/s, rad/s^2):")
            for i in range(count):
                print(f"  J{i + 1}: [{min_pos[i]:.6f}, {max_pos[i]:.6f}], vel={max_vel[i]:.6f}, acc={max_acc[i]:.6f}")
        print(
            "Cartesian limits: "
            f"translation vel={api.getMaxCartTranslationVel(args.ip)} m/s, "
            f"acc={api.getMaxCartTranslationAcc(args.ip)} m/s^2, "
            f"rotation vel={api.getMaxCartRotationVel(args.ip)} rad/s, "
            f"acc={api.getMaxCartRotationAcc(args.ip)} rad/s^2"
        )
    finally:
        destroy_robot(api, args.ip)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
