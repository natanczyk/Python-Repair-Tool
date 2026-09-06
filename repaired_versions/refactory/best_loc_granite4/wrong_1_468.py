def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    if x < seq[0]:
        return 0
    else:
        i = 0
        while i < len(seq):  # Correct the while loop condition
            if x <= seq[i]:
                return i
            elif x > seq[-1]:  # Use -1 index for last element
                return len(seq)
            else:
                i += 1
    return  # Implicitly returns None, but should never reach here