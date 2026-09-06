def search(x, seq):
    counter = 0
    if not seq:
        return 0
    for element in seq:
        if x <= element:
            return counter
        counter += 1
    
    if x > seq[-1]:
        return len(seq)
    
    return counter