from os import makedirs
from pathlib import Path
from site import getsitepackages

import colorama

import configurer
import documenter

from configurer import get_config, config, remove_config, LOCAL, GLOBAL, ALL
#from documenter import open_doc
from toml import load
from typing import Dict, Union, Literal, Any

colorama.init(autoreset=True)

global_config_path = Path.home() / "appdata" / "Roaming" /  "xystudio" / "pyplus" / "config.toml"
local_config_path = Path.cwd() / ".xystudio" / "pyplus" / "config.toml"
global_config: Dict[str, Dict[str, Any]] = {}
local_config: Dict[str, Dict[str, Any]] = {}

NEW = "news"
WILL = "will"

configurer.init(
    default_config_type=LOCAL,
    global_config_path=global_config_path,
    local_config_path=local_config_path,
    must_two_texts=True,
)
configurer.init(default_config_type=configurer.get_config("library", {"firstUsedConfig": LOCAL}).get("firstUsedConfig", LOCAL))

makedirs(global_config_path.parent, exist_ok=True)

if not global_config_path.exists():
    global_config_path.touch()
else:
    with open(global_config_path, 'r', encoding="utf-8") as f:
        global_config = load(f)

if configurer.get_config("library", {"autoCreateLocalConfig": True}).get("autoCreateLocalConfig", True):
    makedirs(local_config_path.parent, exist_ok=True)
    if not(local_config_path.exists()):
        local_config_path.touch()

try:
    with open(local_config_path, 'r', encoding="utf-8") as f:
        local_config = load(f)
except FileNotFoundError:
    pass

first_used_config = configurer.initsettings["default_config_type"]

__all__ = [
    "ALL",
    "LOCAL",
    "GLOBAL",
    "NEW",
    "WILL",
    "get_update",
    "get_version_update_time",
    "get_version",
    "get_pre_version",
    "get_news_update_time",
    "get_new",
    "get_all",
    "get_will",
    "get_pre_update",
    "get_pre_version_update_time",
    "get_pre_news_update_time",
    "get_pre_new",
    "get_pre_all",
    "get_alias",
    "get_doc_help",
    "open_doc",
    "config",
    "get_config",
    "get_config_help",
    "remove_config", 
]

with open(getsitepackages()[1] + "\\pyplus\\data\\config\\update.toml", "r", encoding="utf-8") as f:
    updates = load(f)

with open(
    getsitepackages()[1] + "\\pyplus\\data\\config\\config_help.toml",
    "r",
    encoding="utf-8",
) as f:
    config_help = load(f)

with open(
    getsitepackages()[1] + "\\pyplus\\data\\config\\alias.toml", "r", encoding="utf-8"
) as f:
    lang_alias = load(f)

with open(
    getsitepackages()[1] + "\\pyplus\\data\\config\\doc_help.toml",
    "r",
    encoding="utf-8",
) as f:
    doc_help = load(f)

with open(
    getsitepackages()[1] + "\\pyplus\\data\\config\\deprecated.toml",
    "r",
    encoding="utf-8",
) as f:
    deprecated_modules = load(f)

if configurer.get_config("library", {"showDeprecationWarning": True}).get(
    "showDeprecationWarning", True
) and deprecated_modules:
    for k, v in deprecated_modules.items():
        print(f"{colorama.Fore.YELLOW}{colorama.Style.BRIGHT}warning: {k} module is deprecated scice {v["deprecated_version"]} and will be removed in {v['remove_version']} version.Please use {v['replace_module']} instead.{colorama.Style.RESET_ALL}")
    print(
        f"{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}note:write 'config('library.showDeprecationWarning', 'false')' and run code again to close this warning.{colorama.Style.RESET_ALL}"
    )

def get_update(namespace: str, version: str) -> Union[str, Dict[str, str]]:
    """get the version update doc."""
    try:
        open_dict = updates["release"][namespace]["update_info"]
    except KeyError:
        raise ValueError('This namespace not found.')

    if version == ALL: 
        out_obj: Union[Dict[str, str], str]  = open_dict
    elif version == NEW: 
        out_obj = open_dict.get(updates['release'][namespace]['version'], "This version is not found. Maybe it is not recorded.")
    elif version == WILL: 
        out_obj = open_dict.get(WILL, "This version is not found. Maybe it is not recorded.")
    else: 
        out_obj = open_dict.get(str(version), "This version is not found. Maybe it is not recorded.")
    
    print(out_obj)
    return out_obj

def get_version_update_time(namespace:str, version: str) -> Union[Dict[str, str], str]: 
    '''Get the version update time.'''
    try:
        open_dict = updates["release"][namespace]["update_time"]
    except KeyError:
        raise ValueError('This namespace not found.')

    if version == ALL: 
        out_obj = open_dict
    elif version == NEW: 
        out_obj = open_dict.get(updates['release'][namespace]['version'], "This version is not found. Maybe it is not recorded.")
    elif version == WILL: 
        raise ValueError('`get_version_update_time` cannot get will update time.')
    else: 
        out_obj = open_dict.get(str(version), "This version is not found. Maybe it is not recorded.")
    
    print(out_obj)
    return out_obj

def get_will(namespace:str): 
    '''Get the will update doc.'''
    return get_update(namespace, WILL)

def get_version(namespace:str) -> str:
    '''Get the version.'''
    return updates['release'][namespace]['version']

def get_pre_version() -> str:
    '''Get the pre version.'''
    return updates['pre-release']['version']

def get_news_update_time(namespace:str): 
    '''Get the new update time.'''
    return get_version_update_time(namespace, NEW)

def get_new(namespace:str): 
    '''Get the new update doc.'''
    return get_update(namespace, NEW)

def get_all(namespace:str): 
    '''Get the all update doc.'''
    return get_update(namespace, ALL)

def get_pre_update(version: str) -> Union[Dict[str, str], str]: 
    '''Get the pre-release version update doc.'''
    try:
        open_dict: Dict[str, Any] = updates["pre-release"]["update_info"]
    except KeyError:
        raise ValueError('This namespace not found.')

    if version == ALL: 
        out_obj = open_dict
    elif version == NEW: 
        out_obj = open_dict.get(updates['pre-release']['version'], "This version is not found. Maybe it is not recorded.")
    elif version == WILL: 
        out_obj = open_dict.get(WILL, "This version is not found. Maybe it is not recorded.")
    else: 
        out_obj = open_dict.get(str(version), "This version is not found. Maybe it is not recorded.")

    print(out_obj)
    return out_obj


def get_pre_version_update_time(version: str) -> Union[Dict[str, str], str]:
    """Get the pre-release version update time."""
    try:
        open_dict: Dict[str, Any] = updates["pre-release"]["update_time"]
    except KeyError:
        raise ValueError('This namespace not found.')

    if version == NEW: 
        out_obj = open_dict
    elif version == NEW: 
        out_obj = open_dict.get(updates['pre-release']['version'], "This version is not found. Maybe it is not recorded.")
    elif version == WILL: 
        raise ValueError('`get_version_update_time` cannot get will update time.')
    else: 
        out_obj = open_dict.get(str(version), "This version is not found. Maybe it is not recorded.")
    print(out_obj)
    return out_obj

def get_pre_news_update_time(): 
    '''Get the new update time.'''
    return get_pre_version_update_time(NEW)

def get_pre_new(): 
    '''Get the new pre-release update doc.'''
    return get_pre_update(NEW)

def get_pre_all(): 
    '''Get the all pre-release update doc.'''
    return get_pre_update(ALL)


def open_doc(doc_name: str, lang="en"):
    from markdown import markdown
    from os import remove
    from webbrowser import open as op
    from time import sleep

    doc_html_path = Path.cwd() / ".xystudio" / "pyplus" / "cache" / "doc.html"
    doc_name = doc_name.lower()

    for key, values in lang_alias.items():
        if lang.lower() in values:
            lang = key
    lang = lang.lower()

    makedirs(doc_html_path.parent, exist_ok=True)

    if doc_name == "index":
        op(getsitepackages()[1] + f"\\pyplus\\data\\docs\\web\\{lang}\\index.html")
    else:
        with open(
            getsitepackages()[1]
            + f"\\pyplus\\data\\docs\\markdown\\{lang}\\{doc_name}.md",
            "r",
            encoding="utf-8",
        ) as f:
            html = markdown(f.read())

        with open(doc_html_path, "w", encoding="utf-8") as f:
            f.write(html)

        op(doc_html_path)
        sleep(1)
        remove(doc_html_path)


def get_doc_help(doc_name: str = ALL):
    print()
    if doc_name == ALL:
        for doc_namespace, doc_des in doc_help.items():
            print(f"{doc_namespace} : {doc_des}")
    else:
        print(f"{doc_name}: {doc_help.get(doc_name, 'Not found.')}")


def get_alias(lang: str = ALL):
    print()
    match_alias = None
    for k, v in lang_alias.items():
        if lang.lower() in v:
            match_alias = k
            break

    if lang == ALL:
        for k, v in lang_alias.items():
            print(f"alias {k} -> {', '.join(v)}")
    elif match_alias is not None:
        print(f"alias {match_alias} -> {lang}")
    else:
        print(f"alias {lang} -> {', '.join(lang_alias.get(lang, ["Not found."]))}")


def get_config_help(config_type:Union[str, Literal["all"]] = ALL):
    if config_type == ALL:
        for config_t,config_docs in config_help.items():
            print("*" * 22 + "-" * 8 + config_t + "-" * 8 + "*" * 22)
            for doc_name, doc_des in config_docs.items():
                print()
                print(f"{doc_name} : {doc_des}")
            print(f"\n{'-'*30}\n")
        print(
            "\nWhen you set config,you need use 'pyplus config set local name.config value'"
        )
    else:
        print("*" * 22 + "-" * 8 + config_type + "- " * 8 + "*" * 22)
        try:
            for doc_name, doc_des in config_help[config_type].items():
                print(f"{doc_name} : {doc_des}")
        except KeyError:
            print(f"This config type {config_type} is not found.")
        else:
            print(
                "When you set config,you need use 'pyplus config set local name.config value'"
            )

del Dict, Union, Literal, Any, configurer, Path, makedirs, load, getsitepackages
