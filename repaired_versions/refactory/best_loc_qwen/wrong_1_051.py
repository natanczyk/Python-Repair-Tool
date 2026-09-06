def search(x, seq):
    newseq = list(seq)
    sortlist = []
    if not newseq or newseq[-1] < x:
        return len(newseq)
    while x not in sortlist and newseq:
        start = newseq.pop(0)
        if x <= start:
            sortlist.append(x)
            break
        else:
            sortlist.append(start)
    sortlist.extend(newseq)
    for pos, elem in enumerate(sortlist):
        if elem == x:
            return pos
    return 0