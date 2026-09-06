def search(x, seq):
    pos = len(seq)  # Default to the end if x is greater than all elements
    for i, elem in enumerate(seq):
        if elem >= x:  # Find the first position where elem is not less than x
            pos = i
            break
    return pos