def search(x, seq):
    for count, ele in enumerate(seq):
        if x <= ele:
            return count
    
    return len(seq)