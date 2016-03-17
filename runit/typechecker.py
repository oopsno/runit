def typecheck(signature, value) -> bool:
    """
    :param signature: The type signature e.g. [str], (ind, float), callable
    :param value: The value to check
    :return: whether or not matches
    """
    if isinstance(signature, list):
        # firstly, value must be a list
        if not isinstance(value, list):
            return False
        # check [a]
        elif len(signature) == 1:
            return all(map(lambda x: typecheck(signature[0], x), value))
        # DO NOT SUPPORT [t0, t1, ... , tn]
        else:
            sig = '[{}]'.format(', '.join(map(lambda x: x.__name__, signature)))
            raise TypeError("Cannot type-check on signature {}.".format(sig))
    elif isinstance(signature, tuple):
        if not isinstance(value, tuple):
            return False
        # check for unit '()'
        if len(signature) == 0:
            return value == ()
        # check (t0, t1, ..., tn)
        else:
            return all(map(lambda couple: typecheck(*couple), zip(iter(signature), iter(value))))
    elif signature in [None, NotImplemented, Ellipsis]:
        return value is signature
    else:  # other types
        return isinstance(value, signature)


def typechecker(*args):
    """
    Genrates a typechecker
    :param args: Type signatures
    :return: A typecheker witch will returns 'True' if the value to check
    matches ANY of the signatures
    """

    def _typechecker(value):
        for signature in args:
            if typecheck(signature, value):
                return True
        return False

    return _typechecker
