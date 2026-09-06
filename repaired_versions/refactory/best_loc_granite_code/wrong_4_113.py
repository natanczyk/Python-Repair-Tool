def sort_age(lst):
    out = []
    for ele in lst:
        for indx in range(len(out)):
            if out[indx][1] < ele[1]:
                out.insert(indx, ele)
                break
        else:
            out.append(ele)
    return out