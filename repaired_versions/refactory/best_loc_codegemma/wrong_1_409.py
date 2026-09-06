def search(x, seq):
    for i, element in enumerate(seq):
        if x <= element:  # Fix: Change `<` to `<=` to include equal cases
            return i
    return len(seq)