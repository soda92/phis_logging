from pathlib import Path
import os

def setup_dir():
    cwd = Path.cwd()
    if cwd.joinpath('文档').exists():
        return
    elif cwd.parent.joinpath('文档').exists():
        os.chdir(cwd.parent)
