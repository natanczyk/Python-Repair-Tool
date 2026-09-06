def search(x, seq):
    if len(seq) == 0:
        return 0
    if x == seq[0]:
        return 0
    if x < seq[0]:
        return 0
    if x > seq[0]:
        return search(x, seq[1:]) + 1