#!/usr/bin/env python3
# Copyright (c) 2026 Agile Robots SE
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import add_common_arguments, destroy_robot, detect_and_validate_robot, init_robot, print_joints, print_pose, print_wrench, resolve_robot_profile, robot_state_name
from robots import MAX_SUPPORTED_JOINT_COUNT, print_supported_robot_models


def main() -> int:
    parser = argparse.ArgumentParser(description="Read robot state and diagnostics.")
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
        speeds = [0.0] * MAX_SUPPORTED_JOINT_COUNT
        currents = [0.0] * MAX_SUPPORTED_JOINT_COUNT
        torques = [0.0] * MAX_SUPPORTED_JOINT_COUNT
        pose = [0.0] * 6

        if api.getJointPos(joints, args.ip):
            print("Joint position:")
            print_joints(joints, count)
        if api.getJointAngularVel(speeds, args.ip):
            print("Joint angular velocity (rad/s):")
            for i in range(count):
                print(f"  J{i + 1}: {speeds[i]:.6f}")
        if api.getJointCurrent(currents, args.ip):
            print("Joint current (A):")
            for i in range(count):
                print(f"  J{i + 1}: {currents[i]:.6f}")
        if api.getJointTorque(torques, args.ip):
            print("Joint torque (Nm):")
            for i in range(count):
                print(f"  J{i + 1}: {torques[i]:.6f}")
        if api.getTcpPos(pose, args.ip):
            print("TCP pose:")
            print_pose(pose)

        print(f"TCP external resultant force: {api.getTcpExternalForce(args.ip)} N")
        state = api.getRobotState(args.ip)
        print(f"Robot state: {state} ({robot_state_name(state)})")
        print("Diagnostics:")
        print(f"Link state: {api.getLinkState(args.ip)}")
        print(f"Last error: {api.getLastError(args.ip)}")
        print(f"Last warning: {api.getLastWarning(args.ip)}")
        print(f"Collision detected: {'yes' if api.isCollision(args.ip) else 'no'}")

        tcp_force = [0.0] * 6
        if api.getTcpForce(tcp_force, args.ip):
            print("TCP external wrench:")
            print_wrench(tcp_force)
        joint_force = [0.0] * MAX_SUPPORTED_JOINT_COUNT
        if api.getJointForce(joint_force, args.ip):
            print("Joint external force/torque:")
            for i in range(count):
                print(f"  J{i + 1}: {joint_force[i]:.6f}")
    finally:
        destroy_robot(api, args.ip)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
