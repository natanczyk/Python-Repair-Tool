def search(x, seq):
    if seq == ():
        return 0
    else:
        max_val_index = 0
        for i, element in enumerate(seq):
            if x <= element:
                return i
            max_val_index = i + 1
        return max_val_index