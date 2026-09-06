def search(x, seq):
    """
    Finds the insertion point of x in a sorted sequence seq.

    Args:
        x: The value to search for.
        seq: The sorted sequence to search in.

    Returns:
        The insertion point of x in seq, or 0 if x is not in seq.
    """

    if not seq:
        return 0

    if x > max(seq):
        return len(seq)

    if x < min(seq):
        return 0

    for i, value in enumerate(seq):
        if value >= x:
            return i

    return len(seq)