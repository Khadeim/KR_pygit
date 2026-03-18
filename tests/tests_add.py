import os
import json
from pygit import cli


def test_add_files(tmp_path):

    os.chdir(tmp_path)

    cli.init_repo()

    with open("example.txt", "w") as f:
        f.write("hello")

    cli.add_files(["example.txt"])

    with open(".pygit/index.json") as f:
        index = json.load(f)

    assert "example.txt" in index