def search(x, seq):
    if not seq:
        return 0
    else:
        for i, element in enumerate(seq):
            if x <= element:
                return i
        return seq.index(max(seq)) + 1