def search(x, seq):
    seq = list(seq)  # Ensure seq is a list
    i = 0
    while i < len(seq) and x > seq[i]:
        i += 1
    return i