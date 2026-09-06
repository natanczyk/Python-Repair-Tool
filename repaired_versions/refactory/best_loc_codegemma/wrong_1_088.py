def search(x, seq):
    count = 0
    for i in range (0, len(seq)):
        if seq[i] < x:
            count += 1
    return count if count > 0 else 0