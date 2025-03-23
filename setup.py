from setuptools import setup, find_packages

with open("README-PYPI.md",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="python-plus-tools",
    version="1.0.7.post0",
    packages=find_packages(),
    install_requires=["toml"],
    python_requires=">=3.9,<=3.14",
    author="xystudio",
    author_email="173288240@qq.com",
    description="For the expansion of python content, it covers science, debugging and other fields.",
    long_description=long_description,
    license="MIT",
    url="https://github.com/xystudio889/pyplus",
)
