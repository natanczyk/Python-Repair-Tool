def sort_age(lst):
    out = []
    for ele in lst:
        inserted = False
        for indx in range(len(out)):
            if out[indx][1] < ele[1]:
                out.insert(indx, ele)
                inserted = True
                break
        if not inserted:
            out.append(ele)
    return out