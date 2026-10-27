#!/usr/bin/env python3
# Copyright (c) 2026 Agile Robots SE
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import add_common_arguments, destroy_robot, detect_and_validate_robot, init_robot, resolve_robot_profile
from robots import print_supported_robot_models


def main() -> int:
    parser = argparse.ArgumentParser(description="Read and optionally write controller I/O.")
    add_common_arguments(parser)
    parser.add_argument("--set-do", type=int, choices=(0, 1), help="Write board/do0.")
    parser.add_argument("--set-ao", help="Write board/ao0 as <mode>:<value>.")
    args = parser.parse_args()
    if args.list_models:
        print_supported_robot_models()
        return 0
    profile = resolve_robot_profile(args)
    api = init_robot(args.ip)
    try:
        detect_and_validate_robot(api, args.ip, profile)
        ret, value = api.readDI("board", "di0", args.ip)
        print(f"board/di0 = {value.value}" if ret == 0 else "readDI(board, di0) failed.")
        ret, value = api.readDO("board", "do0", args.ip)
        print(f"board/do0 = {value.value}" if ret == 0 else "readDO(board, do0) failed.")
        ret, mode, value = api.readAI("board", "ai0", args.ip)
        if ret == 0:
            print(f"board/ai0 mode={mode.value} value={value.value}")
        ret, mode, value = api.readAO("board", "ao0", args.ip)
        if ret == 0:
            print(f"board/ao0 mode={mode.value} value={value.value}")
        ret, value = api.readBusCurrent(args.ip)
        if ret == 0:
            print(f"Bus current: {value.value} A")
        ret, value = api.readBusVoltage(args.ip)
        if ret == 0:
            print(f"Bus voltage: {value.value} V")
        if args.set_do is not None:
            print(f"Writing board/do0 = {args.set_do}")
            api.writeDO("board", "do0", args.set_do, args.ip)
        if args.set_ao:
            try:
                mode_text, value_text = args.set_ao.split(":", 1)
                print(f"Writing board/ao0 mode={int(mode_text)} value={float(value_text)}")
                api.writeAO("board", "ao0", int(mode_text), float(value_text), args.ip)
            except ValueError:
                print("Use --set-ao=<mode>:<value>, for example --set-ao=0:0.0", file=sys.stderr)
                return 5
    finally:
        destroy_robot(api, args.ip)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
