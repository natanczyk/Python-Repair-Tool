def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == []:
        return 0
    elif type(seq) == tuple:
        new_seq = list(seq)
        sort = []
        for i in range(len(new_seq)):
            if new_seq[i] < x:
                sort.append(new_seq[i])
            elif new_seq[i] >= x: 
                sort.append(x)
                sort.extend(new_seq[i:])
                break
        else:
            sort.append(x)
    else:
        sort = []
        for i in range(len(seq)):
            if seq[i] < x:
                sort.append(seq[i])
            elif seq[i] >= x: 
                sort.append(x)
                sort.extend(seq[i:])
                break
        else:
            sort.append(x)
    return sort.index(x)