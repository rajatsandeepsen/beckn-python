import os
import shutil

def RemoveFiles(path):
    """
    Remove the file or all files and folders in the specified path.
    """
    if not os.path.exists(path):
        print(f"Path does not exist: {path}")
        return

    if os.path.isfile(path):
        os.remove(path)
        print(f"Removed file: {path}")
    elif os.path.isdir(path):
        # Remove all contents inside the directory
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
                print(f"Removed file: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Removed folder: {item_path}")

list_of_paths = [
    "./package/.github",
    "./package/.openapi-generator",
    "./package/test",
    "./package/.travis.yml",
    # "./package/pyproject.toml",
    "./package/git_push.sh",
    "./package/.gitlab-ci.yml",
    "./package/.openapi-generator-ignore",
    "./package/setup.cfg",
    "./package/setup.py",
    "./package/test-requirements.txt",
    "./package/tox.ini",
    "./package/README.md",
    "./package/docs",
    "./package/requirements.txt",
]

for path in list_of_paths:
    RemoveFiles(path)