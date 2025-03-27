from setuptools import setup, find_packages
import sys

with open("README-PYPI.md",encoding="utf-8") as f:
    long_description = f.read()

data_files = []
if sys.platform == "win32":
    data_files = [('Scripts', ['scripts/pyplus.exe'])]

setup(
    name = "python-plus-tools",
    version = "1.0.8a4",
    packages = find_packages(),
    install_requires = ["toml", "linecode"],#, "indently-decorators"],
    python_requires = ">=3.6,<=3.14",
    author = "xystudio",
    author_email = "173288240@qq.com",
    description = "For the expansion of python content, it covers science, debugging and other fields.",
    long_description = long_description,
    license = "MIT",
    url = "https://github.com/xystudio889/pyplus",
    data_files = data_files,
    include_package_data = True
)
