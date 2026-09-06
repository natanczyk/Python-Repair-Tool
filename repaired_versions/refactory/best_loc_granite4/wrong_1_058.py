def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for num in range(len(seq)):
            if x > seq[num]:
                continue
            elif x <= seq[num]:
                return num 
    return 0