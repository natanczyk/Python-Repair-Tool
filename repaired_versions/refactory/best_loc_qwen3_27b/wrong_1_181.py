def search(x, seq):
    if seq == () or seq == []:
        return 0
    
    for i, elem in enumerate(seq):
        if x > seq[-1]:
            return len(seq)
        elif x > elem:
            continue
        else:
            return i
    
    return len(seq)