def search(x, seq):
    a = list(enumerate(seq))
    seq = list(seq)
    i = 0
    while i < len(seq):
        if x < seq[i] and i == 0:
            return 0
        elif x <= a[i][1] and x >= a[i-1][1]:
            return a[i][0]
        elif x > a[len(seq)-1][1]:
            return len(seq)
        else:
            i = i + 1
            
    # Handle the case when the loop is skipped due to an empty sequence
    return 0