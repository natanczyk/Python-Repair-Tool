def search(x, seq):
    counter = 0
    for element in seq:
        if x <= element:
            return counter
        counter += 1
    return len(seq)