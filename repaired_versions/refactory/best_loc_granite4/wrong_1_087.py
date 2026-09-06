def search(x, seq):
    if not seq:  # Check if the sequence is empty (handles both empty list and tuple)
        return 0
    count = 0
    for element in seq:
        if element < x:
            count += 1
    return count