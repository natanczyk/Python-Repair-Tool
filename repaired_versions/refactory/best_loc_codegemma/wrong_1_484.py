def search(x, seq):
    for i in range(len(seq)):
        if seq[i] >= x:
            return i  # return immediately if found
    return len(seq)  # return the length of the sequence if not found