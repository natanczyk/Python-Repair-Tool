def search(x, seq):
    position = 0
    for i in range(len(seq)):
        if i == 0:
            if x <= seq[i]:
                position = i
        else:
            if x <= seq[i] and x > seq[i-1]:
                position = i
    # Handle the case where x is greater than all elements in the sequence
    if x > seq[-1] if seq else float('inf'):
        position = len(seq)
    return position