def search(x, seq):
    for i in range(0,len(seq)):
        if x<seq[i]:
            return i
            break
        elif x==seq[i]:
            return i
            break
    if not seq:
        return 0
    elif x>seq[len(seq)-1]:
        return len(seq)
    return -1