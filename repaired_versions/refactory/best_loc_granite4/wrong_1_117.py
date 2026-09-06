def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    if x > seq[-1]:  # Use > instead of >= to handle equal to last element
        return len(seq)
    for i, elem in enumerate(seq):
        if elem >= x:
            return i
    return len(seq)  # In case x is greater than all elements