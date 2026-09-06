def search(x, seq):
    if not seq:
        position = 0
    elif x <= seq[0]:
        position = 0
    elif x > seq[-1]:
        position = len(seq)
    else:
        for i in range(1, len(seq)):
            if x <= seq[i] and x > seq[i - 1]:
                position = i
    return position