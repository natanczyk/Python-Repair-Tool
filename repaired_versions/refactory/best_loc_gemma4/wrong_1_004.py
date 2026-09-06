def search(x, seq):
    if not seq:
        return 0
    
    # The goal is to find the index of the first element that is not less than x
    # (essentially implementing bisect_left for a sorted sequence)
    if x <= seq[0]:
        return 0
    if x > seq[-1]:
        return len(seq)
    
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
    return len(seq)