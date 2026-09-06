def search(x, seq):
    for a,b in enumerate(seq):
        if x<=b:
            return a
    if not seq:
        return 0
    for i in seq:
        if x>i:
            return a+1