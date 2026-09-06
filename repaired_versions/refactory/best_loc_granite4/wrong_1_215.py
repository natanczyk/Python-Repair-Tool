def search(x, seq):
    if not seq:  # Check for empty sequence (list or tuple)
        return 0
    elif x <= seq[0]:  # Include equality to handle cases like [5, 5, 5]
        return 0
    elif x > seq[-1]:  # If x is greater than the last element, return length of seq
        return len(seq)
    else:
        for i in range(len(seq) - 1):
            if seq[i] < x <= seq[i + 1]:  # Adjust condition to handle equality correctly
                return i + 1
        return len(seq)  # Fallback, though logically unreachable due to previous checks