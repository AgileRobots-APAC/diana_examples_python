#!/usr/bin/env python3
# Copyright (c) 2026 Agile Robots SE
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import add_common_arguments, detect_and_validate_robot, resolve_robot_profile, robot_state_name
from robots import print_supported_robot_models


def main() -> int:
    parser = argparse.ArgumentParser(description="Diana API connection lifecycle example.")
    add_common_arguments(parser)
    parser.add_argument("--enable", action="store_true", help="Demonstrate releaseBrake and holdBrake.")
    args = parser.parse_args()

    if args.list_models:
        print_supported_robot_models()
        return 0

    profile = resolve_robot_profile(args)
    from common import get_diana_api

    api = get_diana_api()
    print(f"Robot IP: {args.ip}")
    if profile:
        print(f"Requested model: {profile.display_name}")

    error_cb = api.FNCERRORCALLBACK(lambda code, ip: print(f"[Diana API error] code={code}"))
    state_cb = api.FNCSTATECALLBACK(lambda state, ip: None)
    if not api.initSrv([args.ip, 0, 0, 0, 0, 0], error_cb, state_cb):
        print("initSrv failed", file=sys.stderr)
        return 2

    try:
        time.sleep(0.2)
        detect_and_validate_robot(api, args.ip, profile)
        print(f"Diana API library version(raw): {api.getLibraryVersion()}")
        state = api.getRobotState(args.ip)
        print(f"Robot state: {state} ({robot_state_name(state)})")

        if args.enable:
            print("Calling releaseBrake()...")
            if not api.releaseBrake(args.ip):
                return 4
            time.sleep(2)
            print("Calling holdBrake()...")
            api.holdBrake(args.ip)
        else:
            print("Brake state is not changed. Use --enable to demonstrate releaseBrake/holdBrake.")
    finally:
        api.destroySrv(args.ip)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
