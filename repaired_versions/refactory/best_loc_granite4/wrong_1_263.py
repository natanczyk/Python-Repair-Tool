def search(x, seq):
    pos = 0  # Initialize pos to handle empty sequences
    if not seq:  # Check if the sequence is empty
        return pos
    for i in range(len(seq)):
        if x < seq[0]:
            pos = 0
            break
        elif x <= seq[i]:
            pos = i
            break
        elif x > seq[-1]:  # Use -1 index for last element
            pos = len(seq)
            break
    return pos