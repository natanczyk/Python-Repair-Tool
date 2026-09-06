def search(x, seq):
    if not seq:
        return 0
    else:
        i = 0
        for element in seq:
            if x > element:
                i += 1
        return i