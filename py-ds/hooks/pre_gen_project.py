import os
import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
project_slug = "{{ cookiecutter.project_slug }}"

if not re.match(MODULE_REGEX, project_slug):
    print(f"ERROR: {project_slug} is not a valid Python module name!")
    sys.exit(1)

init_git = "{{ cookiecutter.init_git }}"
if init_git == "y":
    os.system("git init")

init_poetry = "{{ cookiecutter.init_poetry }}"
if init_poetry == "y":
    os.system("poetry shell")
