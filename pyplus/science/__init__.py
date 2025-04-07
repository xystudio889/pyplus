'''
This is a moudle for python unit calculation
Use this moudle,plese write: 
`Unit()` or other class in this moudle.
If you want to create new unit class,please use: 
```
class A(ABCUnit)
```
'''

from .units import *
from decimal import Decimal as long
from fractions import Fraction as fraction
from ..tools.update import *
from ..tools.update import upload
from . import shapes
from ..tools.dec import dint,SimpleType

import_all = True

__all__ = [
    "shapes", "fraction", "long", "dint", "SimpleType"
    "get_update", "get_version_update_time", "get_news_update_time", "get_new", "get_all", "get_will", "upload", "ALL", "NEW", "WILL",
    "Unit", "Line", "Area", "Volume", "Capacity", "Duration", "Version", "datetime", "operators"
]

try:
    import numpy, matplotlib
    __all__ += ["numpy","matplotlib"]
except (ImportError, ModuleNotFoundError):
    import_all = False


#if import pyPlus.beta_str,it will be recursion.
beta_str = f"{'This version is not release,update log is prepared.':#^55}\n{'':=^50}\n"
is_databeta_str = f"{'Pre version is this.':#^55}\n{'':=^50}\n"

__version__ = Version(1,0,1)

__update__ = {
    "1.0.1": "Add the ABCUnit,recommed all the class unit(new unit type) use this type.",
    "1.1.0": beta_str + "",
    "1.2.0": beta_str + "Add 'Point','Weight' and new 'Time'.",
    "will": ""
}
__update_time__ = {
    "1.0.0" :  "2025/03/20",
    "1.0.1" :  "2025/03/23",
    "1.1.0" :  "2025/??/??"
}

upload(__version__,__update__,__update_time__)
