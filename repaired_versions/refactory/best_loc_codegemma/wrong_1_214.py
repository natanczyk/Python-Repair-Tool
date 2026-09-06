def search(x, seq):
    
    seq = list(seq)
    max_value = max(seq) if seq else None  # Handle empty sequence
    for i,elem in enumerate(seq):
        if x > max_value:
            seq.insert(seq.index(max_value) + 1,x)
            break
        elif x<elem:
            y = max(0,i)
            seq.insert(y,x)
            break
    if not seq:  # Handle empty sequence
        seq.append(x)
    return seq.index(x)