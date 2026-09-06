def search(x, seq):
    if not seq:
        return 0
    if x <= seq[0]:
        position = 0
    else:
        position = len(seq)
    for i in range(len(seq)):
        if x <= seq[i] and x >= seq[i-1]:
            position = i
            break
    return position