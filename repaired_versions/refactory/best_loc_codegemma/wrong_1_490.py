def search(x, seq):
    if not seq:
        return 0
    l=len(seq)
    for i in range(l):
        if x<=seq[i]:
            break
    if i==l-1 and x>seq[l-1]:
        i=i+1
    return i