# Copyright (c) 2026 Agile Robots SE
# SPDX-License-Identifier: MIT

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class RobotFamily(Enum):
    DIANA = "Diana"
    THOR = "Thor"


@dataclass(frozen=True)
class RobotProfile:
    family: RobotFamily
    key: str
    display_name: str
    joint_count: int


MAX_SUPPORTED_JOINT_COUNT = 7

_PROFILES: tuple[RobotProfile, ...] = (
    RobotProfile(RobotFamily.DIANA, "diana3", "Diana3", 7),
    RobotProfile(RobotFamily.DIANA, "diana7", "Diana7", 7),
    RobotProfile(RobotFamily.DIANA, "diana7-g2", "Diana7 G2", 7),
    RobotProfile(RobotFamily.THOR, "thor7", "Thor7", 6),
    # Thor7 Pro is intentionally not registered yet.
    RobotProfile(RobotFamily.THOR, "thor12", "Thor12", 6),
    RobotProfile(RobotFamily.THOR, "thor20", "Thor20", 6),
)


def _normalize(value: str) -> str:
    return value.strip().lower().replace("_", "-")


def find_robot_profile(model_key: str | None) -> RobotProfile | None:
    if not model_key:
        return None

    key = _normalize(model_key)
    for profile in _PROFILES:
        if key == profile.key:
            return profile

    if key == "diana7g2":
        return find_robot_profile("diana7-g2")

    return None


def iter_robot_profiles() -> Iterable[RobotProfile]:
    return _PROFILES


def robot_family_name(family: RobotFamily) -> str:
    return "Diana series" if family is RobotFamily.DIANA else "Thor series"


def robot_family_name_from_joint_count(joint_count: int) -> str:
    if joint_count == 7:
        return "Diana series"
    if joint_count == 6:
        return "Thor series"
    return "Unknown series"


def print_supported_robot_models() -> None:
    print("Supported robot models:")
    print("  Diana series (7 axes):")
    print("    diana3")
    print("    diana7")
    print("    diana7-g2")
    print("  Thor series (6 axes):")
    print("    thor7")
    print("    thor12")
    print("    thor20")
