def search(x, seq):
    if not seq:
        return 0
    
    seq_list = list(seq)
    for i in range(len(seq_list)):
        if seq_list[i] >= x:
            return i
            
    return len(seq_list)