def search(x, seq):
    if seq == ():
        return 0
    else:
        count = 0
        for element in seq:
            if x > element:
                count += 1
        return count