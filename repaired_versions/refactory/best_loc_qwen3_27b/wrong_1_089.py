def search(x, seq):
    if seq == () or seq == []:
        return 0
    else:
        count = 0
        for i in range(0, len(seq)):
            if seq[i] >= x:
                return i
        return len(seq)