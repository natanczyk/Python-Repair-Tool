def search(x, seq):
    counter = 0
    for i in range(len(seq)):
        if x <= seq[i]:
            counter = i
            break
    else:
        counter = len(seq)
    return counter