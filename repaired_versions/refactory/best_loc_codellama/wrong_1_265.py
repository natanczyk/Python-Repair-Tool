def search(x, seq):
    if seq == () or seq == []:
        return 0
    if seq[0] >= x:
        return 0
    for i in range(len(seq)-1):
        if seq[i] < x and seq[i+1] >= x:
            return i+1
            break
    return len(seq)