def search(x, seq):
    if seq == []:
        return 0
    else:
        for i, element in enumerate(seq):
            if x <= element:
                return i
        return len(seq)