def search(x, seq):
    if not seq:
        return 0
    
    position = len(seq)
    for i in range(len(seq)):
        if x <= seq[i]:
            position = i
            break
            
    return position