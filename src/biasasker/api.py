# src/biasasker/api.py

#from .internal1 import _helper1
#from .internal2 import _helper2

def func1(arg1, arg2):
    """
    Public function 1.
    Internally delegates to _helper1, massages the output, etc.
    """
    result = _helper1(arg1)
    # …maybe combine with arg2, do extra work…
    return result + arg2

def func2(argA):
    """
    Public function 2.
    Internally uses _helper2, maybe reads a file, etc.
    """
    data = _helper2(argA)
    # post-process…
    return {"value": data}
