from itertools import *

def create_generator(values: list):
    return (i for i in values)

def create_generators(*values):
    return (i for i in values)