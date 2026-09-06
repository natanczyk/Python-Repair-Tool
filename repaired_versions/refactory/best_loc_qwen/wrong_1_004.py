def search(x, seq):
    if not seq:
        return 0
    
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        seq_enum = [(i, v) for i, v in enumerate(seq)]
        for j in range(len(seq_enum) - 1):
            if seq_enum[j][1] <= x <= seq_enum[j+1][1]:
                return seq_enum[j][0] if x == seq_enum[j][1] else j + 1

    # If the loop completes without returning, x must be equal to seq[-1]
    return len(seq) - 1