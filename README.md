# Steps to make a barebones pip-installable package

1. Setup your project directory structure
```bash
matt@matt:~/projects$ mkdir mypkg && cd mypkg
matt@matt:~/projects/mypkg$ mkdir mypkg
matt@matt:~/projects/mypkg$ touch setup.py mypkg/my_utils.py mypkg/__init__.py
matt@matt:~/projects/mypkg$ tree
.
├── mypkg
│   ├── __init__.py
│   └── my_utils.py
├── README.md
└── setup.py
```
2. Write your setup.py (nearly-minimal example below)
```python
# in ~/projects/mypkg/setup.py
from setuptools import setup, find_packages
setup(
	author="Matt Triano",
	description="A barebones package.",
	name="mypkg",
	version="0.1.0",
	packages=find_packages(include=["mypkg", "mypkg.*"]),
)
```
3. Put code in the `mypkg/my_utils.py` module (example below)
```python
# in ~/projects/mypkg/mypkg/my_utils.py
import os

def ensure_dir_exists(dir_path: str) -> None:
    """Ensures that a specified directory exists."""
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
```
4. You can leave `mypkg/__init__.py` empty. An `__init__.py` file just tells python to include the other `.py` files in that directory (or *subpackage*) in the namespace of the entire package. Without the `__init__.py` file, the code in `my_utils.py` wouldn't be included in the package (and thus you wouldn't be able to import that code).
