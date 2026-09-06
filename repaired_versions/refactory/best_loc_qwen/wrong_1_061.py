def search(x, seq):
    if len(seq) == 0:
        return 0
    max_index = 0
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
        max_index = i + 1
    return max_index