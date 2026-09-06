def search(x, seq):
    t = 0
    for i in seq:
        if x > i:  # Change the condition to strictly less than
            t += 1

    return t