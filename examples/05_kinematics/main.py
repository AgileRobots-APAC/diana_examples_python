#!/usr/bin/env python3
# Copyright (c) 2026 Agile Robots SE
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import add_common_arguments, destroy_robot, detect_and_validate_robot, init_robot, print_joints, print_pose, resolve_robot_profile
from robots import MAX_SUPPORTED_JOINT_COUNT, print_supported_robot_models


def main() -> int:
    parser = argparse.ArgumentParser(description="Forward/inverse kinematics and rotation conversion.")
    add_common_arguments(parser)
    args = parser.parse_args()
    if args.list_models:
        print_supported_robot_models()
        return 0
    profile = resolve_robot_profile(args)
    api = init_robot(args.ip)
    try:
        count = detect_and_validate_robot(api, args.ip, profile)
        joints = [0.0] * MAX_SUPPORTED_JOINT_COUNT
        if not api.getJointPos(joints, args.ip):
            return 4
        pose = [0.0] * 6
        if api.forward(joints, pose, args.ip):
            print("Forward kinematics result:")
            print_pose(pose)
        inverse_joints = [0.0] * MAX_SUPPORTED_JOINT_COUNT
        if api.inverse(pose, inverse_joints, args.ip):
            print("Inverse kinematics result:")
            print_joints(inverse_joints, count)
        reference_solution = [0.0] * MAX_SUPPORTED_JOINT_COUNT
        if api.inverse_ext(joints, pose, reference_solution, args.ip):
            print("Inverse solution near current joints (inverse_ext):")
            print_joints(reference_solution, count)
        else:
            print("inverse_ext failed.")
        rotation = [math.pi, math.pi / 3.0, math.pi / 6.0]
        print(f"Original RPY: {rotation[0]:.6f}, {rotation[1]:.6f}, {rotation[2]:.6f}")
        if api.rpy2Axis(rotation):
            print(f"Axis-angle vector: {rotation[0]:.6f}, {rotation[1]:.6f}, {rotation[2]:.6f}")
        if api.axis2RPY(rotation):
            print(f"Converted back to RPY: {rotation[0]:.6f}, {rotation[1]:.6f}, {rotation[2]:.6f}")
    finally:
        destroy_robot(api, args.ip)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
