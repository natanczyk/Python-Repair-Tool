def search(x, seq):
    if len(seq) == 0:
        return 0
    elif x > seq[-1]:  # Change from x >= to x >
        return len(seq)
    else:
        for i, elem in enumerate(seq):
            if elem >= x:
                return i
    return len(seq)  # Add this line to handle the case when x is not found in the sequence