def search(x, seq):
    if not seq:  # Check if the sequence is empty at the start
        return 0
    
    a = list(enumerate(seq))
    i = 0
    while i < len(seq):
        if x < seq[i] and i == 0:
            return 0
        elif x <= a[i][1] and x >= a[i-1][1]:
            return a[i][0]
        elif x > a[-1][1]:  # Use -1 to access the last element
            return len(seq)
        else:
            i += 1
    
    return 0  # Return 0 if no condition is met