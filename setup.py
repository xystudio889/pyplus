from setuptools import setup, find_packages

setup(
    name="python-plus-tools",
    version="2.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "toml>=0.10", 
        "indently-decorators>=1.0,<=1.1", 
        "cryptography>=3.4", 
        "imgfit>=0.3", 
        "colorama>=0.1", 
        "deprecated>=1", 
        "typing-extensions>=4.10.0", 
        "numpy>=1.14", 
        "matplotlib>=3.4",
        "torch>=2",
        "pandas>=2",
        "requests>=2.27",
        "sympy==1.13.1",
        "markdown>=3.3.6",
        "numba>=0.55"
    ],
    python_requires=">=3.8",
    author="xystudio",
    author_email="173288240@qq.com",
    description="For the expansion of python content, it covers science, debugging and other fields.",
    long_description=open("README-PYPI.md",encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/xystudio889/pyplus",
    include_package_data=True, 
    entry_points={
        "console_scripts": [
            "pyplus = pyplus_cmd:main",
        ]
    }, 
    extras_require={
        "dev": [
            "tomlconfigure>=0.1",
            "documenter>=0.1",
            "backupworkspace==0.1",
            "python-dotenv>=0.19",
        ],
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-mock",
            "pytest-xdist",
            "coverage",
            "codecov",
            "black",
            "mypy",
            "flake8",
            "pylint",
            "pyright",
        ],
        "build": ["build", "setuptools", "twine"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["debug", "science", "pyplus", "tools", "python"],
)
