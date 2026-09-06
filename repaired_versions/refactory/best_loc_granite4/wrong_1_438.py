def search(x, seq):
    if isinstance(seq, tuple):
        for i, val in enumerate(seq):
            if val >= x:
                return i
        return len(seq)
        
    elif isinstance(seq, list):
        for i, val in enumerate(seq):
            if val >= x:
                return i
        return len(seq)