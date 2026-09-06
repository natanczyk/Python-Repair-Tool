def search(x, seq):
    n = len(seq)
    for i in range(0,n):
        currentvalue = seq[i]
        if x>currentvalue:
            position = i+1
        elif x<= currentvalue:
            return i
    return n