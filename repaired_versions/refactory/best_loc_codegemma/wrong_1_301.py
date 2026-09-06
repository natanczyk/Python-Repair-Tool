def search(x,seq):
    if len(seq) == 0:
        return 0
    for i in range(len(seq)):
        if x > max(seq):
            return len(seq)
        elif x > seq[i]:
            continue
        elif x <= seq[i]:
            break
        
    if i == len(seq):
        return -1
    return i