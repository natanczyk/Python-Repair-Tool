def search(x, seq):
    if list(seq) == []:
        return 0
    elif seq == ():
        return 0
    else:
        for i, element in enumerate(seq):
            if x <= element:
                return i
        return len(seq)