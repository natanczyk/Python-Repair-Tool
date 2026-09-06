def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    a = list(enumerate(seq))
    for item in a:
        if x <= item[1]:
            return item[0]
    return len(seq)