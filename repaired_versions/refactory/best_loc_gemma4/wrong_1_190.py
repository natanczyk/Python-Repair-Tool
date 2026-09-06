def search(x, seq):
    n = len(seq)
    result = 0
    for counter in range(n):
        if seq[counter] >= x:
            result = counter
            break
        else:
            continue
    else:
        # If the loop finishes without breaking, it means all elements 
        # were smaller than x, so the result is the length of the sequence.
        result = n
    return result