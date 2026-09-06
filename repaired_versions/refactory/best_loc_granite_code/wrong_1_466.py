def search(x, seq):
    if not seq:
        return 0
    elif x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        product = 0
        for i in range(len(seq)):
            if x == seq[i]:
                return i
            elif (seq[i] <= x and x <= seq[i+1]):
                product = product + i + 1
        return product