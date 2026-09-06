def search(x, seq):
    if seq == () or seq == []:
        return 0
    else:
        count = 0
        for i in range(len(seq)):
            if seq[i] >= x:
                return count
            count += 1
        return len(seq)