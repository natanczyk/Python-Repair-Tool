def search(x, seq):
    if not seq:
        return 0
    else:
        for index, element in enumerate(seq):
            if x <= element:
                return index
        return len(seq)