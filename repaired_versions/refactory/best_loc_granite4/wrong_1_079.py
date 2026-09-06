def search(x, seq):
    if not seq:  # Check for any empty sequence type
        return 0
    for count, ele in enumerate(seq):
        if x <= ele:
            return count
    if all(x > ele for ele in seq):  # Check if all elements are smaller than x
        return len(seq)