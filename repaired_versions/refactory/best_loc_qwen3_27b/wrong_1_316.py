def search(x, seq):
    for i, ele in enumerate(seq, 0):
        if x > ele:
            i += 1
        else:
            break
    else:
        # This else clause executes if the loop completed without breaking
        # In that case, the insertion point is at the end
        return len(seq)
    return i