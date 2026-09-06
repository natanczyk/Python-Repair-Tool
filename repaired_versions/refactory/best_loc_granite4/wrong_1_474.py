def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    count = 0
    for element in seq:
        if x > element:
            count += 1
    return count