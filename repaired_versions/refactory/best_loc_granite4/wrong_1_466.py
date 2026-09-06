def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    elif x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for i in range(len(seq)):
            if x <= seq[i]:
                return i
        return len(seq)  # Fallback, though logically unreachable due to previous checks