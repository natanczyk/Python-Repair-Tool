def search(x, seq):
    counter = 0
    new_seq = list(seq)
    if not new_seq:  # Check if the sequence is empty
        return 0
    
    for element in new_seq:
        if x <= element:
            return counter
        counter += 1
    
    return len(new_seq)