def search(x,seq):
    for i,elem in enumerate(seq):
        if x <= elem:
            return i
    return len(seq) if seq else 0