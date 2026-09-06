def search(x, seq):
    if not seq:  # Check for any empty sequence
        return 0
    else:
        for i, elem in enumerate(seq):
            if x <= elem:  # Combine the conditions for x < elem and x == elem
                return i
            elif i == len(seq) - 1:
                return i + 1