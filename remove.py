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
    "./beckn/package/.github",
    "./beckn/package/.gitignore",
    "./beckn/package/.openapi-generator",
    "./beckn/package/test",
    "./beckn/package/.travis.yml",
    "./beckn/package/pyproject.toml",
    "./beckn/package/git_push.sh",
    "./beckn/package/.gitlab-ci.yml",
    "./beckn/package/.openapi-generator-ignore",
    "./beckn/package/setup.cfg",
    "./beckn/package/setup.py",
    "./beckn/package/test-requirements.txt",
    "./beckn/package/tox.ini",
    "./beckn/package/README.md",
    "./beckn/package/docs",
    "./beckn/package/requirements.txt",
]

for path in list_of_paths:
    RemoveFiles(path)