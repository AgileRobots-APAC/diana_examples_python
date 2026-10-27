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

GUARDED_MOVE_SECONDS = 10.0
FORCE_POLL_PERIOD_SECONDS = 0.01
FORCE_THRESHOLD_NEWTONS = 5.0


def main() -> int:
    parser = argparse.ArgumentParser(description="Force-threshold guarded motion.")
    add_common_arguments(parser)
    parser.add_argument("--run", action="store_true", help="Execute guarded motion.")
    args = parser.parse_args()
    if args.list_models:
        print_supported_robot_models()
        return 0
    profile = resolve_robot_profile(args)
    require_model_for_run(args, profile)
    api = init_robot(args.ip)
    try:
        detect_and_validate_robot(api, args.ip, profile)
        print(f"Guarded move: base X at 0.01 m/s, stop at |Fx| >= {FORCE_THRESHOLD_NEWTONS} N.")
        if not args.run:
            print("DRY RUN")
            return 0
        if not api.releaseBrake(args.ip):
            return 5
        time.sleep(2)
        ret = api.speedL([0.01, 0.0, 0.0, 0.0, 0.0, 0.0], [0.02, 0.05], GUARDED_MOVE_SECONDS, args.ip)
        force = [0.0] * 6
        stopped_by_force = False
        last_fx = 0.0
        deadline = time.monotonic() + GUARDED_MOVE_SECONDS
        while ret and time.monotonic() < deadline:
            if api.getTcpForce(force, args.ip):
                last_fx = force[0]
                if abs(last_fx) >= FORCE_THRESHOLD_NEWTONS:
                    stopped_by_force = True
                    break
            time.sleep(FORCE_POLL_PERIOD_SECONDS)
        api.stop(args.ip)
        api.holdBrake(args.ip)
        if not ret:
            print("Guarded move command failed.", file=sys.stderr)
            return 6
        if stopped_by_force:
            print(f"Stopped by force threshold: Fx={last_fx} N (threshold=+/-{FORCE_THRESHOLD_NEWTONS} N).")
        else:
            print(f"Stopped by normal timeout after {GUARDED_MOVE_SECONDS} s. Last Fx={last_fx} N.")
    finally:
        destroy_robot(api, args.ip)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
