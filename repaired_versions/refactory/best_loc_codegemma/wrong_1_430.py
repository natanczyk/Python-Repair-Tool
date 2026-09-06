def search(x, seq):
    for i,elem in enumerate(seq):
        if not seq:
            return 0
        elif elem>=x:
            return i
        elif i+1==len(seq):
            return len(seq)
        else:
            continue
    return 0