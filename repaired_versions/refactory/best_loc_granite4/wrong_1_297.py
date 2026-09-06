def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    for i, val in enumerate(seq):
        if x > val:
            continue
        else:
            break
    else:
        # If the loop completes without breaking, x is greater than all elements
        return len(seq)
    return i  # Return 0-based index