import os
import json
import sys

PYGIT_DIR = ".pygit"
CONFIG_FILE = "config.json"

def init_repo():
    """Initialise a new PyGit repository."""
    if os.path.exists(PYGIT_DIR):
        print("Repository already initialised!")
        return

    # Create .pygit folder
    os.makedirs(PYGIT_DIR)

    # Initialise configuration
    config = {
        "current_branch": "main",
        "branches": {"main": None}  # HEAD points to latest commit hash
    }

    # Save config.json
    with open(os.path.join(PYGIT_DIR, CONFIG_FILE), "w") as f:
        json.dump(config, f, indent=4)

    # Create objects folder to store commits later
    os.makedirs(os.path.join(PYGIT_DIR, "objects"))
    
    print(f"Initialised empty PyGit repository in {os.path.abspath(PYGIT_DIR)}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <command>")
        return

    command = sys.argv[1]
    if command == "init":
        init_repo()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()