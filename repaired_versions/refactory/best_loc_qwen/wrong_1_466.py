def search(x, seq):
    if seq == () or seq == []:
        return 0
    elif x < seq[0]:
        return 0
    elif x > seq[len(seq) - 1]:
        return len(seq)
    else:
        for i in range(len(seq)):
            if x == seq[i]:
                return i
            elif seq[i] < x <= seq[i + 1] if i + 1 < len(seq) else x > seq[i]:
                return i + 1