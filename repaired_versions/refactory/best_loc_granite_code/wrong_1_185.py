def search(x, seq):
    for i in range(len(seq)):
        if x>seq[i]:
            continue
        else:
            return i
    return len(seq)