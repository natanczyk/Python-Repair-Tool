def sort_age(lst):
    # Fill in your code here
    if not lst:
        return lst
        
    out = [lst[0],]
    for ele in lst[1:]:
        inserted = False
        for indx in range(len(out)):
            if out[indx][1] < ele[1]:
                out.insert(indx, ele)
                inserted = True
                break
        if not inserted:
            out.append(ele)
    return out