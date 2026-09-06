def search(x, seq):
    count = 0
    while count < len(seq) and seq[count] < x:
        count += 1
    return count