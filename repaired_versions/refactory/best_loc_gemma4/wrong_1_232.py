def search(x, seq):
    if seq == () or seq == []:
        return 0
    if x <= seq[0]:
        return 0
    if x > seq[len(seq)-1]:
        return len(seq)
    
    # Special case for the last element to avoid IndexError in the loop
    if x == seq[len(seq)-1]:
        return len(seq) - 1
        
    for i in range(len(seq) - 1):
        if seq[i] <= x <= seq[i+1]:
            return i + 1