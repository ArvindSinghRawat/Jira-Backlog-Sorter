import subprocess
import os
import sys

import platform


def activate_virtual_env(env):
    """Activates a virtual environment.

    Args:
      env: The path to the virtual environment.
    """

    if platform.system() == "Windows":
        var = [os.sep.join([env, "Scripts", "activate.bat"])]
        print(var)
        subprocess.call(var)
    elif os.name == "posix" or platform.system() == "darwin":
        subprocess.call(["source", env + "/bin/activate"])
    elif platform.system() == "Linux":
        subprocess.call(["source", env + "/bin/activate"])
    else:
        print(f"Platform `{sys.platform}` and System `{platform.system()}` undefined")


if __name__ == "__main__":
    path_to_env = os.getenv("BUILD_VENV", None)
    if path_to_env is not None:
        activate_virtual_env(path_to_env)
