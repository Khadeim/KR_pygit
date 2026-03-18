import os
import json
import sys

PYGIT_DIR = ".pygit"
CONFIG_FILE = "config.json"
INDEX_FILE = "index.json"

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

    # Create empty staging index
    with open(os.path.join(PYGIT_DIR, INDEX_FILE), "w") as f:
        json.dump([], f)
    
    print(f"Initialised empty PyGit repository in {os.path.abspath(PYGIT_DIR)}")

def load_index():
    """Load staged files from the index."""
    with open(os.path.join(PYGIT_DIR, INDEX_FILE), "r") as f:
        return json.load(f)

def save_index(index):
    """Save staged files to the index."""
    with open(os.path.join(PYGIT_DIR, INDEX_FILE), "w") as f:
        json.dump(index, f, indent=4)

def add_files(files):
    """Stage files for commit."""
    
    if not os.path.exists(PYGIT_DIR):
        print("Error: repository not initialised.")
        return

    index = load_index()

    for file in files:

        if not os.path.exists(file):
            print(f"Warning: {file} does not exist.")
            continue

        if file not in index:
            index.append(file)
            print(f"Staged {file}")
        else:
            print(f"{file} already staged.")

    save_index(index)

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <command>")
        return

    command = sys.argv[1]
    if command == "init":
        init_repo()
    elif command == "add":
        if len(sys.argv) < 3:
            print("Usage: python cli.py add <file1> <file2> ...")
        else:
            add_files(sys.argv[2:])
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()