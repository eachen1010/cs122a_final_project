import os
import sys
import subprocess
import tomllib
import venv
from pathlib import Path

VENV_DIR = Path("baggie")

def create_venv():
    if not VENV_DIR.exists():
        print("Creating virtual environment...")
        venv.EnvBuilder(with_pip=True).create(VENV_DIR)
    else:
        print("Virtual environment already exists.")

def venv_python():
    """Return path to the python inside the venv."""
    if os.name == "nt":  # Windows
        return VENV_DIR / "Scripts" / "python.exe"
    else:  # macOS/Linux
        return VENV_DIR / "bin" / "python"

def load_dependencies():
    print("Reading pyproject.toml...")
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)

    project = data.get("project", {})
    deps = project.get("dependencies", [])

    # Optional: include optional dependency groups
    opt_groups = project.get("optional-dependencies", {})
    for group, group_deps in opt_groups.items():
        print(f"Including optional dependency group: {group}")
        deps.extend(group_deps)

    return deps

def install_dependencies(python, deps):
    if not deps:
        print("No dependencies found in pyproject.toml")
        return

    print("Upgrading pip...")
    subprocess.check_call([python, "-m", "pip", "install", "--upgrade", "pip"])

    print("Installing dependencies...")
    subprocess.check_call([python, "-m", "pip", "install"] + deps)

def main():
    create_venv()
    python = venv_python()

    deps = load_dependencies()
    install_dependencies(python, deps)

    print("\nDone! Virtual environment is ready.")
    print(f"Activate it using:")
    if os.name == "nt":
        print(r"  venv\Scripts\activate")
    else:
        print("  source venv/bin/activate")

if __name__ == "__main__":
    main()
