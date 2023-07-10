#!/usr/bin/python3
"""
this module checks if a object is an
instance of a class that inherites from

"""


def is_kind_of_class(obj, a_class):
    """
    this function or mothod returns true if the
    object is a instance of a class that inherited
    from a class

    Args:
       obj: object to check
       a_class: class to check in
    Returns:
        True if the object is an instance of,
        or if the object is an instance of a
        class that inherited from

    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
