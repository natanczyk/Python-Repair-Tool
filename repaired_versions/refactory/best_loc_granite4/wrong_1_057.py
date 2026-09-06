def search(x, seq):
    if not seq:  # Handles both empty lists and empty tuples
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for i, num in enumerate(seq):
            if x <= num:
                return i
    return len(seq)  # Return len(seq) if x is greater than all elements