def search(x, seq):
    n = len(seq)
    if not seq:  # if seq is an empty list/tuple
        return 0
    for i in range(n):
        next_element = seq[i]
        if x <= next_element:
            return i
    return n