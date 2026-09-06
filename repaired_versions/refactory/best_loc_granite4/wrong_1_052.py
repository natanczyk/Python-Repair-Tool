def search(x, seq):
    if not seq:  # Handles both empty tuple and empty list
        return 0

    newseq = list(seq)
    sortlist = []
    while newseq:
        start = newseq[0]
        if x <= start:
            sortlist.append(x)
            sortlist.extend(newseq)
            break
        else:
            sortlist.append(start)
            newseq.pop(0)
    else:
        sortlist.append(x)
    
    for pos, elem in enumerate(sortlist):
        if elem == x:
            return pos