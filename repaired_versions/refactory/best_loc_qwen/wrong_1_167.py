def search(x, seq):
    if seq == () or seq == []:
        return 0
    for i in range(len(seq)):
        if x <= seq[i]:
            break
    else:
        i = len(seq)
    return i