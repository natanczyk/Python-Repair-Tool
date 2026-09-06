def search(x, seq):
    
    seq = list(seq)
    if not seq:
        return 0
    max_value = max(seq)
    for i, elem in enumerate(seq):
        if x > max_value:
            seq.insert(seq.index(max_value) + 1, x)
            break
        elif x < elem:
            y = max(0, i)
            seq.insert(y, x)
            break
    else:
        # If the loop completes without breaking, x is >= all elements
        # Insert at the end
        seq.append(x)
    return seq.index(x)