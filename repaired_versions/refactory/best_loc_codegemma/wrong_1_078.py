def search(x, seq):
    for count, ele in enumerate(seq):
        if x<=ele:
            return count
        
    if not seq:
        return 0
    
    for ele in seq:
        if x>ele:
            return len(seq)