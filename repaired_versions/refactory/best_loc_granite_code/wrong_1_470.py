def search(x, seq):
    if not seq:
        return 0
    else:
        for i, element in enumerate(seq):
            if x > element:
                i += 1
            else:
                break
        return i