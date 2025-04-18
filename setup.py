from setuptools import setup, find_packages

setup(
    name="python-plus-tools",
    version="1.3.0.dev2",
    packages=find_packages(),
    install_requires=[
        "toml>=0.10", "indently-decorators>=1.0,<=1.1", "cryptography>=3.4", "imgfit>=0.3", "colorama>=0.1", 
        "numpy>=1.14", "matplotlib>=3.4","torch>=2", "pandas>=2", "requests>=2.27"
        ],
    python_requires=">=3.7",
    author="xystudio",
    author_email="173288240@qq.com",
    description="For the expansion of python content, it covers science, debugging and other fields.",
    long_description=open("README-PYPI.md",encoding="utf-8").read(),
    license="MIT",
    url="https://github.com/xystudio889/pyplus",
    include_package_data=True, 
    entry_points={
        "console_scripts": [
            "pyplus = pyplus.__init__:main",
#           "pyplus-config = pyplus.__init__:main_config"
        ]
    }, 
    extras_require={
    "dev": ["deprecated>=1"],
    "test": ["pytest", "mypy"],
    }
)
