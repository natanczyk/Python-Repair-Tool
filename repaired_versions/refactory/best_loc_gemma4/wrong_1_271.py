def search(x, seq):
    position = 0
    while position < len(seq):
        if seq[position] == x:
             return position
        elif seq[position] > x:
            return position
        position = position + 1
    return position