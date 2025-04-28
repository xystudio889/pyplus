'''
The python Plus - Pyplus
================
the python's plus library.\n
'''

from os import makedirs, getenv
from pathlib import Path
from site import getsitepackages

from . import tools, science
from sys import version_info
from toml import load,dump

if version_info > (3,8):
    from typing import List, Dict, Union,Literal, Any
else:
    from typing_extensions import List, Dict, Union, Literal, Any

global_config_path = Path(getenv("appdata"),"xystudio", "pyplus", "config.toml")
local_config_path = Path(".xystudio", "pyplus", "config.toml").absolute()
global_config: Dict[str, Any] = {}
local_config: Dict[str, Any] = {}
union_config: Dict[str, Any] = {}

LOCAL = "local"
GLOBAL = "global"

ALL = "all"
NEW = "news"
WILL = "will"

makedirs(global_config_path.parent, exist_ok=True)

if not global_config_path.exists():
    global_config_path.touch()
else:
    with open(global_config_path, 'r', encoding="utf-8") as f:
        global_config = load(f)

if global_config.get("library", {"autoCreateLocalConfig" : True}).get("autoCreateLocalConfig", True):
    makedirs(local_config_path.parent, exist_ok=True)
    if not(local_config_path.exists()):
        local_config_path.touch()

try:
    with open(local_config_path, 'r', encoding="utf-8") as f:
        local_config = load(f)
except FileNotFoundError:
    pass

first_used_config: Literal["local", "global"] = global_config.get("library", {"firstUsedConfig" : "local"}).get('firstUsedConfig', "local")

if first_used_config == "local":
    union_config = global_config | local_config
else:
    union_config = local_config | global_config

if union_config.get("library", {"showDeprecationWarning" : True}).get("showDeprecationWarning", True):
    print(f"{tools.colors.Fore.MAGENTA}{tools.colors.Style.BRIGHT}note:write 'config('library.showDeprecationWarning', 'false')' and run code again to close this warning.")

if union_config.get("import", {"pyscience" : True}).get("pyscience", True):
    from advancedlib import _all as advancedlib
elif union_config.get("import", {"advancedlib" : True}).get("advancedlib", True):
            from advancedlib import _no_math

__all__ = [
    "science" ,"tools",
    "ALL", "NEW", "WILL", 
    "get_update", "get_version_update_time", "get_version", "get_pre_version", "get_news_update_time", "get_new", "get_all", "get_will", "get_pre_update", "get_pre_version_update_time", "get_pre_news_update_time", "get_pre_new", "get_pre_all", 
    "config", "get_config", "get_config_help"
]

with open(getsitepackages()[1] + "\\pyplus\\data\\config\\update.toml", "r", encoding="utf-8") as f:
    updates = load(f)

with open(getsitepackages()[1] + "\\pyplus\\data\\config\\get_config.toml", "r", encoding="utf-8") as f:
    config_help = load(f)

def get_update(namespace:str, version: str) -> Union[str, Dict[str, str]]: 
    '''get the version update doc.'''
    try:
        open_dict: Dict[str, str] = updates['release'][namespace]['update_info']
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
        open_dict: Dict[str, str] = updates['release'][namespace]['update_time']
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
        open_dict: Dict[str, Any] = updates['pre-release']['update_info']
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
    '''Get the pre-release version update time.'''
    try:
        open_dict: Dict[str, Any] = updates['pre-release']['update_time']
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

def open_doc(doc_name:str):
    raise NotImplementedError("Document is not completed.")

def config(config_name:str, value:Any, config_type: Literal["local", "global"] = first_used_config):
    global local_config,global_config

    if config_type == LOCAL:
        makedirs(local_config_path.parent, exist_ok=True)
        if not(local_config_path.exists()):
            local_config_path.touch()

        config_split = config_name.split(".", 1)
        config_char_1 = config_split[0]
        try:
            config_char_2 = config_split[1]
        except IndexError:
            raise ValueError("config name must use 'a.b'.")

        with open(local_config_path, "w+", encoding="utf-8") as f:
            config = load(f) | {config_char_1 : {config_char_2 : value}}
            local_config |= config
            dump(config, f)
    elif config_type == GLOBAL:
        config_split = config_name.split(".")
        config_char_1 = config_split[0]
        try:
            config_char_2 = config_split[1]
        except IndexError:
            raise ValueError("config name must use 'a.b'.")

        with open(global_config_path, "w+", encoding="utf-8") as f:
            config = load(f) | {config_char_1 : {config_char_2 : value}}
            global_config |= config
            dump(config, f)
    else:
        raise ValueError("This config type not found.")
    union_config |= config

def get_config(config_name:str) -> Union[None, Dict[str, Any]]:
    try:
        config_split = config_name.split(".")
        config_char_1 = config_split[0]
        try:
            config_char_2 = config_split[1]
            return union_config[config_char_1][config_char_2]
        except IndexError:
            raise ValueError("config name must use two texts, example : 'a.b'.")
    except KeyError:
        return None

def get_config_help(config_type:Union[str, Literal["all"]] = ALL):
    if config_type == ALL:
        for config_t,config_docs in config_help.items():
            print("*" * 22 + "-" * 8 + config_t + "-" * 8 + "*" * 22)
            for doc_name, doc_des in config_docs.items():
                print()
                print(f"{doc_name} : {doc_des}")
            print(f"\n{'-'*30}\n")
        print("\nWhen you set config,you need use 'paragraph name.config name'")
    else:
        print("*" * 22 + "-" * 8 + config_type + "- " * 8 + "*" * 22)
        try:
            for doc_name, doc_des in config_help[config_type].items():
                print(f"{doc_name} : {doc_des}")
        except KeyError:
            print("This document is not found.")
        else:
            print("When you set config,you need use 'paragraph name.config name'")

__version__ = get_version("main")

del getsitepackages, Path, getenv, version_info
