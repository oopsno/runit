def typecheck(signature, value) -> bool:
    """
    :param signature: The type signature e.g. [str], (ind, float), callable
    :param value: The value to check
    :return: whether or not matches
    """
    if isinstance(signature, list):
        if len(signature) == 0:  # []
            return isinstance(value, list)
        elif len(signature) == 1:  # [a]
            return all(map(lambda x: typecheck(signature[0], x), value))
    elif isinstance(signature, tuple):
        if len(signature) == 0:  # (), unit
            return value == ()
        else:  # (t0, t1, ..., tn)
            typecheck(list(signature), list(value))
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
