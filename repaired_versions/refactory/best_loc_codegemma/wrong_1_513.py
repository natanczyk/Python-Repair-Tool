def search(x, seq): 
    if not seq:
        return 0
    for i in range(len(seq)): 
        if int(x) < seq[0]:
            return 0    
        elif int(x) > seq[len(seq)-1]:
            return len(seq)        
        elif int(x) > seq[i]:
            continue        
        else:
            return i
    return len(seq)