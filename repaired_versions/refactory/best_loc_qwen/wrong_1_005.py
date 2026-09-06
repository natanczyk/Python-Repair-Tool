def search(x, seq):
    if not seq:
        return 0
    elif x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        seq_enum = [i for i in enumerate(seq)]
        for j in range(len(seq_enum)):
            if x == seq_enum[j][1]:
                return j
            elif x > seq_enum[j][1]:
                continue
            else:
                return j