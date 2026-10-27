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

from common import add_common_arguments, destroy_robot, detect_and_validate_robot, init_robot, print_joints, require_model_for_run, resolve_robot_profile, wait_move
from robots import MAX_SUPPORTED_JOINT_COUNT, print_supported_robot_models


def main() -> int:
    parser = argparse.ArgumentParser(description="Joint paths and waypoints.")
    add_common_arguments(parser)
    parser.add_argument("--run", action="store_true", help="Execute the path.")
    parser.add_argument("--complex", action="store_true", help="Use complex path APIs.")
    args = parser.parse_args()
    if args.list_models:
        print_supported_robot_models()
        return 0
    profile = resolve_robot_profile(args)
    require_model_for_run(args, profile)
    api = init_robot(args.ip)
    try:
        count = detect_and_validate_robot(api, args.ip, profile)
        start = [0.0] * MAX_SUPPORTED_JOINT_COUNT
        if not api.getJointPos(start, args.ip):
            return 5
        target = start[:]
        target[0] += (15.0 if args.complex else 10.0) * math.pi / 180.0
        print(f"{'Complex-path' if args.complex else 'Path'} waypoint 1:")
        print_joints(target, count)
        print("Path waypoint 2 (return to current joints):")
        print_joints(start, count)
        if not args.run:
            print(f"DRY RUN: no {'complex path' if args.complex else 'path'} command sent.")
            return 0
        if not api.releaseBrake(args.ip):
            return 6
        time.sleep(2)
        ret = True
        if args.complex:
            ret_code, path_id = api.createComplexPath(api.complex_path_type.NORMAL_JOINT_PATH, args.ip)
            ret = ret_code == 0
            if ret:
                ret = api.addMoveJSegmentByTarget(path_id, target, 0.10, 0.20, 0.0, 0, 0.0, 0.0, args.ip)
            if ret:
                ret = api.addMoveJSegmentByTarget(path_id, start, 0.10, 0.20, 0.0, 0, 0.0, 0.0, args.ip)
            if ret:
                ret = api.runComplexPath(path_id, args.ip)
        else:
            ret_code, path_id = api.createPath(1, args.ip)
            ret = ret_code == 0
            if ret:
                ret = api.addMoveJ(path_id, target, 0.10, 0.20, 0.0, args.ip)
            if ret:
                ret = api.addMoveJ(path_id, start, 0.10, 0.20, 0.0, args.ip)
            if ret:
                ret = api.runPath(path_id, args.ip)
        if ret:
            wait_move(api, args.ip)
            print("Path finished.")
        else:
            print("Path setup or execution failed.", file=sys.stderr)
            api.stop(args.ip)
        if args.complex:
            api.destroyComplexPath(path_id, args.ip)
        else:
            api.destroyPath(path_id, args.ip)
        api.holdBrake(args.ip)
        return 0 if ret else 7
    finally:
        destroy_robot(api, args.ip)


if __name__ == "__main__":
    raise SystemExit(main())
