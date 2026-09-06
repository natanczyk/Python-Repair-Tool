def search(x, seq):
    if not seq:  # Check if the sequence is empty (handles both [] and ())
        return 0
    for i in range(len(seq)):
        if x == seq[i]:
            return i
        elif x < seq[i]:
            return i
    return len(seq)