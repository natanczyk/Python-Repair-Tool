def search(x, seq):
    if list(seq) == []:
        return 0
    else:
        for element in seq:
            if x <= element:
                return list(seq).index(element)
        return (list(seq).index(max(seq)))+1