def search(x, seq):
    y = len(seq)
    if y == 0:
        return 0
    else:
        # Check if x is less than or equal to the first element
        if x <= seq[0]:
            return 0
        # Check if x is greater than the last element
        if x > seq[-1]:
            return y
        # Search for the position where x fits
        for i in range(y - 1):
            if x > seq[i] and x <= seq[i + 1]:
                return i + 1
        return y