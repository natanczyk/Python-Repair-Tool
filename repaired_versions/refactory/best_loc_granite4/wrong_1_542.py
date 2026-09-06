def search(x, seq):
    if not seq:  # Check if seq is empty (handles both () and [])
        indx = 0
    else:
        if x < seq[0]:
            indx = 0
        elif x > seq[-1]:
            indx = len(seq)  # Use len(seq) instead of seq.index(seq[-1]) + 1
        else:
            for i, value in enumerate(seq):
                if x <= value:
                    indx = i
                    break
    return indx