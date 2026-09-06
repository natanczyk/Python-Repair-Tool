def search(x, seq):
    if len(seq) == 0:
        return 0
    if x <= seq[0]:
        return 0
    if x > seq[-1]:
        return len(seq)

    for i in range(len(seq)):
        if x == seq[i]:
            return i
        elif x > seq[i] and (i == len(seq) - 1 or x < seq[i + 1]):
            return i + 1

    return None