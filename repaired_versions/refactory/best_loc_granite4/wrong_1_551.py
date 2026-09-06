def search(x, seq):
    if not seq:  # Check for any empty sequence (list or tuple)
        return 0
    if x > seq[-1]:
        return len(seq)
    for i in range(len(seq)):
        if x > seq[i]:
            continue
        return i