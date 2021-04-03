# Steps to make a barebones pip-installable package

1. Setup your project directory structure (on Windows, you can replace `touch` with `echo > filename` to create empty files). The `tree` step isn't necessary, it just shows the directory structure.
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
	* In the notebook in `examples/Importability_demo.ipynb`, I explore the effects of leaving `mypkg/__init__.py` blank and provide deeper explanation of the 

5. Now you can install this package in envs where you will use the package (`geo_env` in the example below). While you're still developing your package, use the `-e` flag (e: editable) so changes to the source code will be immediately available for importation (ie without reinstalling the package).
```bash
(geo_env) matt@matt:~/projects/mypkg$ python -m pip install -e .
```
or if you've pushed it to GitHub or GitLab and already set up an access token for your machine, you can install the current version of the main branch via the command below.
```bash
(geo_env) matt@matt:~<any location>$ python -m pip install -e git+ssh://git@github.com/MattTriano/mypkg.git#egg=mypkg
```
Or install a specific branch (eg `hotfix1`) or commit via
```bash
(geo_env) matt@matt:~<any location>$ python -m pip install -e git+ssh://git@github.com/MattTriano/mypkg.git@hotfix1#egg=mypkg
(geo_env) matt@matt:~<any location>$ python -m pip install -e git+ssh://git@github.com/MattTriano/mypkg.git@8740a0cfd7a57d70ae95f79e10160253bcf68d8c#egg=mypkg
```
	* Note: While it's possible to simply install things via `(geo_env) matt@matt:~/projects/mypkg$ pip install -e .`, it's a better practice to include `python -m`. In systems where there are multiple installed versions of python (and potentially multiple installs of `pip`) there can be ambiguity about which version of `pip` is used, and this can cause a package to get installed into the `site-packages` directory for a different python version (which you would discover when you call `import mypkg` and it returns `ModuleNotFoundError`). Including `python -m` eliminates this issue.
	* When you're done developing the package, you can just reinstall the package via any of the above methods, just without the `-e` flag.
6. If the package is going to remain private, you can just create/update the README file in your package's repo and in the **Install Instructions**, remove the `-e` flag from the install command, and grant access permissions to others who you want to use the package.
```bash
(geo_env) matt@matt:~<any location>$ python -m pip install git+ssh://git@github.com/MattTriano/mypkg.git#egg=mypkg
```




N. Should you want to uninstall the package from an enviroment (eg: `geo_env`), just run 
```bash
(geo_env) matt@matt:~$ python -m pip uninstall mypkg
```