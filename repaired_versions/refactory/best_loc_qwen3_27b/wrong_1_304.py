def search(x, seq):
    if type(seq) == list:
        a = seq.copy()
        a.append(x)
        a.sort()
        for i, elem in enumerate(a):
            if elem == x:
                return i
    else:
        temp_tuple = seq + (x,)
        sorted_tuple = sorted(temp_tuple)
        for i, elem in enumerate(sorted_tuple):
            if elem == x:
                return i