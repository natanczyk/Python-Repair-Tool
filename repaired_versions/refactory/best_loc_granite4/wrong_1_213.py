def search(x, seq):
    index = 0
    def helper(index):
        if not seq:
            return 0
        elif index >= len(seq) or x <= seq[index]:
            return index
        else:
            return helper(index + 1)
    return helper(index)