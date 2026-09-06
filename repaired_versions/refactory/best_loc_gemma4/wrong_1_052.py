def search(x, seq):
    if seq == () or seq == []:
        return 0
    
    newseq = list(seq)
    if newseq[-1] < x:
        return len(newseq)
    
    sortlist = []
    while x not in sortlist and newseq:
        start = newseq[0]
        if x <= start:
            sortlist.append(x)
            break
        else:
            sortlist.append(start)
            newseq.pop(0)
            
    if x not in sortlist:
        sortlist.append(x)
        
    for pos, elem in enumerate(sortlist):
        if elem == x:
            return pos