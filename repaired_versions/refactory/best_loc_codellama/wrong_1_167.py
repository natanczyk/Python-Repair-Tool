def search(x, seq):
    if not seq:
        return 0
    for i in range(len(seq)):
        if x <= seq[i]:
            break
    else:
        i += 1
    return i