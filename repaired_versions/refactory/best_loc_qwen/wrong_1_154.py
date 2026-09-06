def search(x, seq):
    a = 0
    for a, b in enumerate(seq):
        if x <= b:
            return a
    if a == 0 and not seq:  # Check if the sequence is empty
        return 0
    else:
        return a + 1