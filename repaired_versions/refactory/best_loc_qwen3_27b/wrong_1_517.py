def search(x, seq):
    if len(seq) == 0:
        return 0
    elif x >= seq[len(seq)-1]:
        # Check if x is actually in the sequence at the end or beyond
        # We need to find the first occurrence of x, or the insertion point
        # Let's do a proper sequential search
        for i in range(len(seq)):
            if x <= seq[i]:
                return i
        return len(seq)
    else:
        for i in range(len(seq)):
            if x > seq[i]:
                continue
            else:
                return i