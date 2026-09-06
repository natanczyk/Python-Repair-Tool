def search(x, seq):
    l=len(seq)
    if l == 0:
        return 0
    for i in range(l):
        if x<=seq[i]:
            break
    else:
        # This part executes if the loop finishes without breaking
        # meaning x is greater than all elements in seq
        return l
    return i