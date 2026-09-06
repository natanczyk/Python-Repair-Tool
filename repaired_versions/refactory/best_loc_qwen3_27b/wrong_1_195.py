def search(x, seq):
    # Handle empty sequence cases first
    if seq == ():
        return 0
    elif seq == []:
        return 0
    
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    
    # If x is greater than all elements, return the length of the sequence
    return len(seq)