def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    if x <= seq[0]:
        return 0
    elif x > seq[-1]:  # Use > to match the expected behavior for values greater than the last element
        return len(seq)
    else:
        for i in range(len(seq) - 1):
            if seq[i] < x <= seq[i + 1]:
                return i + 1
        return None