def search(x, seq):
    if seq == [] or seq == ():
        return 0
    for count, ele in enumerate(seq):
        if x <= ele:
            return count
    return len(seq)