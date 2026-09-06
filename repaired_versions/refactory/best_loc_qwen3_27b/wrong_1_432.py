def search(x, seq):
    if type(seq) == tuple:
        if len(seq) == 0:
            seq = (x,)
        else:
            for i in range(len(seq)):
                if x <= seq[i]:
                    seq = seq[:i] + (x,) + seq[i:]
                    break
            else:
                seq = seq + (x,)

    elif type(seq) == list:
        if len(seq) == 0:
            seq = [x]
        else:
            for i in range(len(seq)):
                if x <= seq[i]:
                    seq = seq[:i] + [x] + seq[i:]
                    break
            else:
                seq = seq + [x]

    for i in enumerate(seq):
        if x == i[1]:
            return i[0]