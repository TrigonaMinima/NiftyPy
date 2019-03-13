#!python

# Will automatically run at Python interpreter startup
print("(startup.py doing its magic)")
import sys
sys.path.insert(0, "/Almost700/Git/tminima/NiftyPy/")
from nifty import *
sys.path.pop(0)
print("(nifty imported)")
