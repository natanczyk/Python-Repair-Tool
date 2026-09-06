def search(x, seq):
    lst = list(seq)
    # Insert x into the sorted list at the correct position
    # We need to find the first index where lst[i] >= x
    inserted = False
    for i in range(len(lst)):
        if x < lst[i]:
            lst.insert(i, x)
            inserted = True
            break
    if not inserted:
        lst.append(x)
    
    # Now find the index of x in the list
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1