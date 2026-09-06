def search(x, seq):
    if not seq:
        return 0
    if x <= seq[0]:
        position = 0
    for i in range(1, len(seq)):
        if x <= seq[i] and x > seq[i-1]:
            position = i
    if x > seq[-1]:
        position = len(seq)
    return position