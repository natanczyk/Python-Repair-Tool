def search(x, seq):
    if not seq:
        return 0
    
    seq_list = list(seq)
    for i, element in enumerate(seq_list):
        if x <= element:
            return i
            
    return len(seq_list)