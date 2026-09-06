def search(x, seq):
    if not seq:
        return 0
    
    # Check if x is less than the first element
    if x < seq[0]:
        return 0
    
    # Check if x is greater than the last element
    if x > seq[-1]:
        return len(seq)
    
    # Search for the position where x fits
    for i in range(len(seq)):
        if seq[i] == x:
            return i
        elif seq[i] < x < seq[i + 1] if i + 1 < len(seq) else False:
            return i + 1
    
    # If x equals the last element
    if x == seq[-1]:
        return len(seq) - 1
    
    return len(seq)