def search(x, seq):
    count = 0
    while count < len(seq):
        if seq[count] < x:
            count += 1
        else:
            return count
    return count