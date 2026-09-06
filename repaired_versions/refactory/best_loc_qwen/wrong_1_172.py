def search(x, seq):
    if not seq:
        return 0
    
    index = 0
    for element in seq:
        if x <= element:
            return index
        index += 1
    
    return index