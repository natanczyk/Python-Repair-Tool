def search(x, seq):
    count = 0
    for i in range(len(seq)):
        if seq[i] < x:
            count += 1
    return count