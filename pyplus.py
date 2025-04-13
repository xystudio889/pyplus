# Will add in 1.2.2.

from sys import argv
from os import system

system(f"python -m pyplus {' '.join(argv[1:])}")