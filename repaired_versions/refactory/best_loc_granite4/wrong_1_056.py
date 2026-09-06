def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    if x > seq[-1]:
        return len(seq)
    else:
        for i, num in enumerate(seq):
            if x <= num:
                return i
    return len(seq)  # In case x is greater than all elements