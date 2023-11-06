#!/usr/bin/python3
"""
a function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ;
otherwise False.
"""


def inherits_from(obj, a_class):
    """Prototype: def inherits_from(obj, a_class):
    for exemple :
        #!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

     ./4-main.py
True inherited from class int
True inherited from class object"""

    if not type(obj) is a_class and isinstance(obj, a_class):
        return True

    return False
