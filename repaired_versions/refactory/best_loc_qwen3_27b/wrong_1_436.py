def search(x, seq):
    count = 0
    for i in seq:
        if i < x:
            count += 1
        else:
            break
    return count