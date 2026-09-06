def search(x, seq):
    if not seq:
        return 0
    
    # The goal of a sequential search for the insertion point or first occurrence
    # in a sorted sequence is to find the index where x would be placed.
    # Based on the failing tests:
    # search(100, []) == 0
    # search(5, [5, 5, 5]) == 0
    
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
            
    return len(seq)