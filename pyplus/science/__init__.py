'''
This is a moudle for python unit calculation
Use this moudle,plese write: 
`Unit()` or other class in this moudle.
If you want to create new unit class,please use: 
'''


from pathlib import Path
from os import getenv

from . import units
from . import pyscience
from . import pyscience as science

from colorama import Style, Fore, init
from toml import load 

init(autoreset=True)

try:
    o1 = open(Path(getenv("appdata"),"xystudio", "pyplus", "config.toml"))
    o2 = open(Path(".xystudio", "pyplus", "config.toml").absolute())

    config = (load(o1) | load(o2)).get("library", {"showDeprecationWarning":True})['showDeprecationWarning']

    o1.close()
    o2.close()
except FileNotFoundError:
    config = True

if config:
    print(Fore.YELLOW + "DeprecationWarning: pyplus.science.science is deprecated since v1.2 and will be removed in v2.0. Please use pyplus.scince.pyscince." + Style.RESET_ALL)
    print(Fore.YELLOW + "DeprecationWarning: pyplus.science.units.operators is deprecated since v1.2 and will be removed in v2.0. Please use pyplus.scince.operator." + Style.RESET_ALL)

del Style, Fore, init, load, getenv

__all__ = [
    "units", "pyscience", "science",
    "Unit", "Line", "Area", "Volume", "Capacity", "Duration", "Version", "datetime", "operators"
]
