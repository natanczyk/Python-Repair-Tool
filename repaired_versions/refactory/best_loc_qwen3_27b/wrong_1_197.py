def search(x, seq):
    count = 0
    while count < len(seq):
        if x > seq[count]:
            count += 1
            continue
        else:
            # x <= seq[count]
            # If x == seq[count], return count (the index of the element)
            # If x < seq[count], return count (the insertion point)
            return count
    return len(seq)