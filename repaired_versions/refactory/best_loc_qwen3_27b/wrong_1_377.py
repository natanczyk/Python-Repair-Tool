def search(x, seq):
    lst1 = list(seq)
    if lst1 == []:
        return 0
    else: 
        length = len(lst1)
        if x < lst1[0]:
            return 0
        elif x > lst1[length - 1]:
            return length
        else:
            for i in range(0, length):
                if lst1[i] == x:
                    return i
                if lst1[i] < x < lst1[i + 1]:
                    return i + 1
            # If x equals the last element
            if lst1[-1] == x:
                return length - 1
    return -1