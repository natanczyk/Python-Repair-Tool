def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    for index, element in enumerate(seq):
        if x <= element:
            return index
    return len(seq)