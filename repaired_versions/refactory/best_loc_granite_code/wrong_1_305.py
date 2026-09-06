def search(x, seq):
    for i,v in enumerate(seq):
        if x>v:
            continue
        else:
            return i
    return len(seq)