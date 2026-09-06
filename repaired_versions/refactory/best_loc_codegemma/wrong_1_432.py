def search(x, seq):
    if not seq:
        return 0

    if type(seq) == tuple:
        for i in range(len(seq)):
            if x <= seq[i]:
                seq = seq[:i] + (x,) + seq[i:]
            elif seq[len(seq)-1] < x:
                seq = seq + (x,)

    elif type(seq) == list:
        for i in range(len(seq)):
            if x <= seq[i]:
                seq = seq[:i] + [x,] + seq[i:]
            elif seq[len(seq)-1] < x:
                seq = seq + [x,]

    for i, value in enumerate(seq):
        if x == value:
            return i