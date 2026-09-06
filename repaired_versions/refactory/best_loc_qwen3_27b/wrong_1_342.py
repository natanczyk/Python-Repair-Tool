def search(x, seq):
    # Handle empty sequence case
    if not seq:
        return 0
    
    for i in range(len(seq)):
        if x == seq[i]:
            return i
        elif x < seq[i]:
            return i
    
    return len(seq)