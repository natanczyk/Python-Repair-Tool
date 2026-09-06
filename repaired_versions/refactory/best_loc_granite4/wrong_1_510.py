def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    if x > seq[-1]:  # Use -1 index for the last element
        return len(seq)
    for i in range(len(seq)):
        if x > seq[i]:
            continue
        return i