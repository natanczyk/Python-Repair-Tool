def search(x, seq):
    a = list(enumerate(seq))
    seq = list(seq)
    i = 0
    while i < len(seq):
        if x < seq[i] and i == 0:
            return 0
        elif x <= a[i][1] and x >= a[i-1][1]:
            return a[i][0]
        elif x > a[-1][1]:  # Use -1 to access the last element
            return len(seq)
        else:
            i += 1
            
    return 0  # Return 0 when the loop finishes or is skipped (e.g., empty list)