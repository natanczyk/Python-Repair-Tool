def search(x, seq):
    count = 0
    for element in seq:
        if element < x:
            count += 1
    return count