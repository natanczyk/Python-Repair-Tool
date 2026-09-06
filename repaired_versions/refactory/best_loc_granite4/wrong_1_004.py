def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        # Find the first occurrence of x or the position where x should be inserted
        for i, value in enumerate(seq):
            if value >= x:
                return i
        return len(seq)