def sort_age(lst):
    # Fill in your code here
    out = []
    for ele in lst:
        indx = 0
        while indx < len(out) and out[indx][1] >= ele[1]:
            indx += 1
        out.insert(indx, ele)
    return out