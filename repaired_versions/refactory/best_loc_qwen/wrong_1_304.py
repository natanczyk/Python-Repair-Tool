def search(x, seq):
    if type(seq) == list:
        a = seq + [x]
        a.sort()
        for i, elem in enumerate(a):
            if elem == x:
                return i
    else:
        temp_tuple = seq + (x,)
        for i, elem in enumerate(sorted(temp_tuple)):
            if elem == x:
                return i