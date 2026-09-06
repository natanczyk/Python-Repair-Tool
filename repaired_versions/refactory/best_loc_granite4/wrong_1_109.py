def search(x, seq):
    if len(seq) == 0:
        return 0
    elif x <= seq[0]:
        return 0
    elif x > seq[-1]:  # Change >= to >
        return len(seq)
    else:
        for i, val in enumerate(seq):
            if x <= val:
                return i
        return None