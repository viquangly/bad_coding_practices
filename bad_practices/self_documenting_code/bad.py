
def do_something(l, c, y, h):
    a = 780
    b = 650
    aa = 10
    bb = 5

    z = y / l

    if h or (c >= a) or (z >= aa):
        return True
    
    if c >= b:
        return z >= bb
    else:
        return z >= aa
