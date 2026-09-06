def search(x, seq):
    count = 0
    for element in seq:
        if seq == ():
            return 0
        elif x > element:
            count += 1
    return count