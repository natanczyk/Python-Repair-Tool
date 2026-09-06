def search(x, seq):
    position = 0
    if not seq:
        return position
    
    for i in range(len(seq)):
        if x <= seq[i]:
            position = i
            break
    
    # If x is greater than all elements in the sequence, place it at the end
    if position == 0 and x > seq[0]:
        position = len(seq)
    
    return position