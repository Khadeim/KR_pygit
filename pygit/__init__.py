import os
import shutil
from pygit import cli

def test_init_repo(tmp_path):
    os.chdir(tmp_path)  # Use temporary directory
    cli.init_repo()
    
    assert os.path.exists(".pygit")
    assert os.path.exists(".pygit/config.json")
    assert os.path.exists(".pygit/objects")

    # Check contents of config.json
    import json
    with open(".pygit/config.json") as f:
        config = json.load(f)
    assert config["current_branch"] == "main"
    assert "main" in config["branches"]