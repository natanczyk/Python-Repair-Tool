def search(x, seq):
    if not seq:  # Check if the sequence is empty (handles both empty list and empty tuple)
        return 0
    for i, v in enumerate(seq):
        if x > v and i != len(seq) - 1:
            continue
        elif x > v and i == len(seq) - 1:
            return i + 1
        else:
            break
    return i