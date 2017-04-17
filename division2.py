def div(x, y):
    """ my division function """
    m = 0
    r = x
    while (True):
        if r >= y:
            m += 1
            r -= y
        else:
            break
    return (m, r)
