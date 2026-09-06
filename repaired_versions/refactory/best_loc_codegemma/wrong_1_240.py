def search(x, seq):
    n = len(seq)
    insertion_index = n
    for i in range(0,n):
        currentvalue = seq[i]
        position = i
        if position >= 0 and x>currentvalue:
            insertion_index = i
        elif position >= 0 and x<= currentvalue:
            return position
    if not seq:
        return 0
    if x > seq[-1]:
        return n
    return insertion_index