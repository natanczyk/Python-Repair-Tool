def search(x, seq):
    if len(seq) == 0:
        return 0
    else:     
        for i in range(len(seq)):
            if x <= seq[i]:
                return i
         
        return len(seq)