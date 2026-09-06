def search(x, seq):
    for i in range(len(seq)):
        if int(x) < seq[0]:
            return 0
        elif int(x) > seq[i]:
            continue
        else:
            return i
    return len(seq)