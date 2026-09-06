def search(x, seq):
    count = 0
    for elem in seq:
        if elem < x:
            count += 1
        else:
            break
    return count