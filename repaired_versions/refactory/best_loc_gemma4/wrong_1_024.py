def search(x, seq):
    if not seq:
        return 0
    elif x < int(seq[0]):
        return 0
    elif x > int(seq[len(seq)-1]):
        return len(seq)
    else:
        for i in range(len(seq)):
            if x == seq[i]:
                return i
            if i + 1 < len(seq) and x > seq[i] and x <= seq[i+1]:
                return i+1
        return len(seq)