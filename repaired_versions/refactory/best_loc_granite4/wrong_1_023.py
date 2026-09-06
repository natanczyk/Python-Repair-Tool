def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    if x <= int(seq[0]):
        return 0
    if x > int(seq[-1]):
        return len(seq)
    for i in range(len(seq) - 1):
        if seq[i] < x <= seq[i + 1]:
            return i + 1
    return len(seq)