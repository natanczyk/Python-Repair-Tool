def search(x, seq):
    no = 0
    for i in range(0, len(seq)):
        if x > seq[i]:
            continue
        elif x <= seq[i]:
            no = i
            return no
    
    # If the loop completes without returning, x is greater than all elements
    # or the sequence is empty.
    if len(seq) == 0:
        return 0
    return len(seq)