def flatten(sequence):
    f = []
    for x in sequence:
        if isinstance(x, (list, tuple)):
            f += flatten(x)
        else:
            f.append(x)
    return f