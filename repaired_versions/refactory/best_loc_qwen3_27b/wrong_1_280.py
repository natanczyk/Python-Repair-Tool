def search(x, seq):
    # Handle empty sequence
    if len(seq) == 0:
        return 0
    
    # Check if x is less than or equal to the first element
    if x <= seq[0]:
        return 0
    
    # Check if x is greater than the last element
    if x > seq[-1]:
        return len(seq)
    
    # Search for the position where x fits
    for i in range(len(seq) - 1):
        if seq[i] < x <= seq[i + 1]:
            return i + 1
    
    # If x equals the last element or falls between last-1 and last
    # This handles cases where x == seq[-1]
    if x == seq[-1]:
        return len(seq) - 1
    
    return len(seq)