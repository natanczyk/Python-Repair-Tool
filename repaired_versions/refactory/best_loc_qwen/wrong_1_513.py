def search(x, seq): 
    Index = 0
    for i in range(len(seq)): 
        if int(x) < seq[0]:
            return 0    
        elif int(x) > seq[len(seq)-1]:
            return len(seq)        
        elif int(x) <= seq[i]:
            return i
    return len(seq)