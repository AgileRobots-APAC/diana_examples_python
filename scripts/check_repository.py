#!/usr/bin/env python3
# Copyright (c) 2026 Agile Robots SE
# SPDX-License-Identifier: MIT

from __future__ import annotations

import ast
import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SDK_DIR = Path(os.environ.get("DIANA_SDK_DIR", ROOT / "third_party" / "diana_sdk_python")).expanduser()
SDK_WRAPPER = SDK_DIR / "lib" / "DianaApi.py"
PYTHON_DIRS = (ROOT / "common", ROOT / "robots", ROOT / "examples")
MARKDOWN_DIRS = (ROOT / "docs", ROOT / "examples")
MARKDOWN_LINK = re.compile(r"\[[^]]*\]\(([^)]+)\)")


def python_files() -> list[Path]:
    return sorted(path for directory in PYTHON_DIRS for path in directory.rglob("*.py"))


def check_python_syntax(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in paths + [SDK_WRAPPER]:
        try:
            ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
        except (OSError, SyntaxError) as exc:
            errors.append(f"Python syntax: {path.relative_to(ROOT)}: {exc}")
    return errors


def sdk_public_names() -> set[str]:
    tree = ast.parse(SDK_WRAPPER.read_text(encoding="utf-8-sig"))
    names: set[str] = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(node.name)
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Name):
                    names.add(target.id)
    return names


def check_sdk_references(paths: list[Path]) -> list[str]:
    exported = sdk_public_names()
    errors: list[str] = []
    for path in paths:
        tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Attribute)
                and isinstance(node.value, ast.Name)
                and node.value.id == "api"
                and node.attr not in exported
            ):
                errors.append(
                    f"SDK reference: {path.relative_to(ROOT)}:{node.lineno}: "
                    f"DianaApi.{node.attr} does not exist"
                )
    return errors


def markdown_files() -> list[Path]:
    root_files = [ROOT / "README.md", ROOT / "README.cn.md", ROOT / "CHANGELOG.md"]
    nested = [path for directory in MARKDOWN_DIRS for path in directory.rglob("*.md")]
    return sorted(path for path in root_files + nested if path.is_file())


def check_markdown_links(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in paths:
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for raw_target in MARKDOWN_LINK.findall(line):
                target = raw_target.strip().split("#", 1)[0]
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                if not (path.parent / target).resolve().exists():
                    errors.append(
                        f"Markdown link: {path.relative_to(ROOT)}:{line_number}: "
                        f"missing {raw_target}"
                    )
    return errors


def check_bilingual_docs() -> list[str]:
    errors: list[str] = []
    english_docs = [
        path
        for directory in MARKDOWN_DIRS
        for path in directory.rglob("*.md")
        if not path.name.endswith(".cn.md")
    ]
    for path in sorted(english_docs):
        chinese = path.with_name(f"{path.stem}.cn.md")
        if not chinese.exists():
            errors.append(f"Bilingual docs: missing {chinese.relative_to(ROOT)}")
    return errors


def check_example_clis() -> list[str]:
    errors: list[str] = []
    for path in sorted((ROOT / "examples").glob("*/main.py")):
        result = subprocess.run(
            [sys.executable, str(path), "--list-models"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        if result.returncode != 0:
            errors.append(
                f"Example CLI: {path.relative_to(ROOT)} exited {result.returncode}: "
                f"{result.stderr.strip()}"
            )
    return errors


def main() -> int:
    paths = python_files()
    errors = [
        *check_python_syntax(paths),
        *check_sdk_references(paths),
        *check_markdown_links(markdown_files()),
        *check_bilingual_docs(),
        *check_example_clis(),
    ]
    if errors:
        print("Repository checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Repository checks passed ({len(paths)} Python files, 12 example CLIs).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
