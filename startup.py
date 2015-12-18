#!/media/248GB/System/anaconda3/bin/python

# Will automatically run at Python interpreter startup
print("(startup.py doing its magic)")
import sys
sys.path.insert(0, "/media/248GB/git/TrigonaMinima/NiftyPy/")
from nifty import *
sys.path.pop(0)
print("(nifty imported)")
