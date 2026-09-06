def search(x, seq):
    position = 0
    for eleme in seq:
        if x <= eleme:
            break
        position += 1
    return position