def search(x, seq):
    count = 0
    while count < len(seq):
        if seq[count] >= x:
            break
        count += 1
    return count