def search(x, seq):
    i = 0
    while i < len(seq):
        if x <= seq[i]:
            break
        i += 1
    else:
        i = len(seq)
    
    return i