from setuptools import setup, find_packages
import sys

data_files = [('Scripts', [])]

if sys.platform == "win32":
    data_files = [('Scripts', [])]

setup(
    name="python-plus-tools",
    version="1.2.0rc3",
    packages=find_packages(),
    install_requires=["toml>=0.10", "indently-decorators>=1.0,<=1.1", "cryptography>=3.4", "imgfit>=0.3", 
                      "numpy>=1.14", "matplotlib>=3.4","torch>=2", "pandas>=2"],
    python_requires=">=3.8",
    author="xystudio",
    author_email="173288240@qq.com",
    description="For the expansion of python content, it covers science, debugging and other fields.",
    long_description=open("README-PYPI.md",encoding="utf-8").read(),
    license="MIT",
    url="https://github.com/xystudio889/pyplus",
    data_files=data_files,
    include_package_data=True
)
