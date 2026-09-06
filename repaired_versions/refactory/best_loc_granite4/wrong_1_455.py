def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    if len(seq) == 1:
        return 0 if seq[0] >= x else 1
    if seq[-1] < x:  # Corrected condition to handle the case when x is greater than the last element
        return len(seq)
    if seq[0] >= x:
        return 0
    for i in range(len(seq) - 1):  # Adjusted range to avoid IndexError
        if seq[i] < x <= seq[i + 1]:
            return i + 1
    return len(seq)  # Handle the case when x is equal to the last element