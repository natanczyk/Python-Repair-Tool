def search(x, seq): 
    if not seq:  # Check if the sequence is empty
        return 0
    
    if int(x) < seq[0]:
        return 0    
    elif int(x) > seq[-1]:
        return len(seq)  

    index = 0
    for i in range(len(seq)): 
        if int(x) > seq[i]:
            index = i + 1
        else:
            break
    return index