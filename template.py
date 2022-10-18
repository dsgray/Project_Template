
# help with OS independence
import os
from pathlib import Path

# help with debugging
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s: %levelname)s]: %(message)s'
    )

while True:
    project_name = input("Enter the Project Name: ")
    if project_name != '':
        break

logging.info(f"Creating project by name: {project_name}")

# Create list of files
# ".github/workflows/.gitkeep": empty file needed for Github with dummy file
# that will be replaced later
# src: keep all scripts
# init: create a repository (conda environment setup)
# requirements: testing on different environments

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # works for any system
    if filedir != "": # check if just a file
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filename} at path {filepath}")
    else: # file already there
        logging.info(f"file is already present at: {filepath}")
