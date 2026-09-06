def search(x, seq):
    if not seq:
        return 0
    
    if x < seq[0]:
        indx = 0
    elif x > seq[-1]:
        indx = len(seq)
    else:
        for i in range(len(seq)):
            if x <= seq[i]:
                indx = i
                break                    
    return indx