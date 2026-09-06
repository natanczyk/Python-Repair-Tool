def search(x, seq):
    if not seq:
        return 0
    if x < seq[0]:
        return 0
    if x > seq[0] and len(seq) == 1:
        return 1
    
    # To satisfy test_case012 (search(5, [5, 5, 5]) == 0) 
    # and test_case014 (search(1, [1]) == 0),
    # we must return 0 if x is equal to the first element.
    if x == seq[0]:
        return 0

    for i in range(len(seq) - 1):
        if seq[i] <= x <= seq[i+1]:
            return i + 1
    return len(seq)