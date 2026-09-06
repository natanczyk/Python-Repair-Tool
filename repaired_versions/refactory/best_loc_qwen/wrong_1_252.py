def search(x, seq):
    if not seq:
        position = 0
    else:
        if x <= seq[0]:
            position = 0
        else:
            for i in range(1, len(seq)):
                if x <= seq[i]:
                    position = i
                    break
            else:
                position = len(seq)
    return position