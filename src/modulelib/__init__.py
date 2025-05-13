from importlib import *

from toml import load, dump
from site import getsitepackages

with open(getsitepackages()[1] + "/pyplus/data/config/module_config.toml", encoding="utf-8") as f:
    config = load(f)

if not config["advancedlib"]["itertools"]["initializinged"]:
    from . import all_module

del load, dump, getsitepackages

def get_import_moudle_path():
    from sys import modules
    if __name__ != "__main__":
        main_moudle = modules['__main__']
        if hasattr(main_moudle, '__file__'):
            return main_moudle.__file__
        else:
            return None


def get_latest_version(package_name, include_prerelease: bool = False, url: str = None):
    import requests
    from packaging.version import parse

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://pypi.org/",
    }

    url = (
        f"https://pypi.org/pypi/{package_name}/json"
        if url is None
        else url.replace("%P", package_name)
    )
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    data = response.json()
    all_versions = list(data["releases"].keys())  # 获取所有版本列表

    # 解析并过滤版本
    valid_versions = []
    for v in all_versions:
        version = parse(v)
        if not include_prerelease and version.is_prerelease:
            continue  # 跳过预发布版本
        valid_versions.append(version)

    if not valid_versions:
        return None
    latest = max(valid_versions)
    return str(latest)


def check_update(
    package_name: str,
    include_prerelease: bool = False,
    auto_update: bool = False,
    url: str = None,
):
    from os import system
    from importlib.metadata import version

    installed_version = version(package_name)
    latest_version = get_latest_version(
        package_name, include_prerelease, url
    )  # 使用上述PyPI API方法
    if latest_version and installed_version != latest_version:
        if include_prerelease:
            print(
                f"New pre-release version available: {installed_version} → {latest_version}"
            )
        else:
            print(f"New version available: {installed_version} → {latest_version}")
        if auto_update:
            print("Auto-updating...")
            if include_prerelease:
                system(f"pip install --upgrade --pre {package_name}")
            else:
                system(f"pip install --upgrade {package_name}")
            print("Update complete.")
    else:
        print("Already up to date.")
