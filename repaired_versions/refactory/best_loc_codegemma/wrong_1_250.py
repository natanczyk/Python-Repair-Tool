def search(x, seq):
    if not seq or x <= seq[0]:
        position = 0
    else:
        position = 1
    for i in range(1, len(seq)):
        if x <= seq[i] and x > seq[i-1]:
            position = i
        elif x > seq[-1]:
            position = len(seq)
    return position