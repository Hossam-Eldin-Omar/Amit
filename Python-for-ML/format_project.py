import os
import subprocess


def autopep_format(root):
    for folder, subfolders, files in os.walk(root):
        subfolders[:] = [
            d for d in subfolders if d not in {
                "venv", ".venv", "__pycache__"}]
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(folder, f)
                print("Formatting:", path)
                subprocess.run(["autopep8", "--in-place",
                               "--aggressive", "--aggressive", path])


if __name__ == "__main__":
    autopep_format(".")
