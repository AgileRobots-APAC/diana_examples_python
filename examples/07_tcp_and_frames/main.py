#!/usr/bin/env python3
# Copyright (c) 2026 Agile Robots SE
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import add_common_arguments, destroy_robot, detect_and_validate_robot, init_robot, print_pose, resolve_robot_profile
from robots import print_supported_robot_models


def parse_offset(text: str | None) -> list[float]:
    if not text:
        return [0.0] * 6
    values = [float(part) for part in text.split(",")]
    if len(values) != 6:
        raise argparse.ArgumentTypeError("--offset must contain 6 comma-separated values")
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description="Read TCP, frames, payload, and calculate a tool-relative offset.")
    add_common_arguments(parser)
    parser.add_argument("--offset", type=parse_offset, default=[0.0] * 6, help="x,y,z,roll,pitch,yaw; angles in degrees.")
    args = parser.parse_args()
    if args.list_models:
        print_supported_robot_models()
        return 0
    profile = resolve_robot_profile(args)
    api = init_robot(args.ip)
    try:
        detect_and_validate_robot(api, args.ip, profile)
        tcp_pose = [0.0] * 6
        tcp_pose_ok = api.getTcpPos(tcp_pose, args.ip)
        if tcp_pose_ok:
            print("Current TCP pose:")
            print_pose(tcp_pose)
        else:
            print("getTcpPos failed; tool-relative target pose cannot be calculated.", file=sys.stderr)
        active_tcp_pose = [0.0] * 6
        if api.getDefaultActiveTcpPose(active_tcp_pose, args.ip):
            print("Default active TCP pose relative to flange:")
            print_pose(active_tcp_pose)
        active_tcp = [0.0] * 16
        if api.getDefaultActiveTcp(active_tcp, args.ip):
            print("Default active TCP homogeneous matrix:")
            for row in range(4):
                print("  " + " ".join(f"{active_tcp[row * 4 + col]:.6f}" for col in range(4)))
        ret, default_tcp = api.getDefaultTcpCoordinate(args.ip)
        if ret:
            print(f"Default TCP coordinate: {default_tcp}")
        else:
            print("getDefaultTcpCoordinate failed.", file=sys.stderr)
        ret, default_workpiece = api.getDefaultWorkPieceCoordinate(args.ip)
        if ret:
            print(f"Default workpiece coordinate: {default_workpiece}")
        else:
            print("getDefaultWorkPieceCoordinate failed.", file=sys.stderr)
        payload = [0.0] * 10
        if api.getActiveTcpPayload(payload, args.ip):
            print("Active TCP payload:")
            print(f"  mass={payload[0]:.6f} kg")
            print(f"  center=({payload[1]:.6f}, {payload[2]:.6f}, {payload[3]:.6f}) m")
            print(
                "  inertia="
                f"({payload[4]:.6f}, {payload[5]:.6f}, {payload[6]:.6f}, "
                f"{payload[7]:.6f}, {payload[8]:.6f}, {payload[9]:.6f})"
            )
        rotation = [v * math.pi / 180.0 for v in args.offset[3:]]
        rotation_ok = api.rpy2Axis(rotation)
        offset_axis = args.offset[:3] + rotation
        current_matrix = [0.0] * 16
        offset_matrix = [0.0] * 16
        target_matrix = [0.0] * 16
        target_pose = [0.0] * 6
        if tcp_pose_ok and rotation_ok and api.pose2Homogeneous(tcp_pose, current_matrix) and api.pose2Homogeneous(offset_axis, offset_matrix):
            for row in range(4):
                for col in range(4):
                    target_matrix[row * 4 + col] = sum(current_matrix[row * 4 + k] * offset_matrix[k * 4 + col] for k in range(4))
            if api.homogeneous2Pose(target_matrix, target_pose):
                print("Tool-relative target pose:")
                print_pose(target_pose)
        print("Read-only example: no TCP, payload, or coordinate configuration is modified.")
    finally:
        destroy_robot(api, args.ip)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
