def search(x, seq):
    if isinstance(seq, tuple):
        inserted = False
        for i in range(len(seq)):
            if x <= seq[i]:
                seq = seq[:i] + (x,) + seq[i:]
                inserted = True
                break
        if not inserted and (not seq or x > seq[-1]):
            seq = seq + (x,)
        for i, val in enumerate(seq):
            if val == x:
                return i

    elif isinstance(seq, list):
        inserted = False
        for i in range(len(seq)):
            if x <= seq[i]:
                seq.insert(i, x)
                inserted = True
                break
        if not inserted and (not seq or x > seq[-1]):
            seq.append(x)
        for i, val in enumerate(seq):
            if val == x:
                return i

    # Handle empty sequence case
    if not seq:
        return 0