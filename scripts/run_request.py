"""Bootstrap a new self-contained project folder.

Usage:
    python scripts/run_request.py <project-name>

Example:
    python scripts/run_request.py pendo-onboarding

Creates:
    projects/YYYYMMDD_<project-name>/
        data/raw/
        data/processed/
        notebooks/
        outputs/
"""
import sys
from datetime import date
from pathlib import Path


def create_project(name: str) -> Path:
    today = date.today().strftime("%Y%m%d")
    folder_name = f"{today}_{name}"
    root = Path(__file__).parent.parent / "projects" / folder_name

    if root.exists():
        print(f"Project already exists: projects/{folder_name}/")
        return root

    for sub in ["data/raw", "data/processed", "notebooks", "outputs"]:
        subdir = root / sub
        subdir.mkdir(parents=True, exist_ok=True)
        (subdir / ".gitkeep").touch()

    print(f"Created: projects/{folder_name}/")
    print("Next: add your notebooks, run scripts, and outputs there.")
    return root


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/run_request.py <project-name>")
        sys.exit(1)
    create_project(sys.argv[1])
