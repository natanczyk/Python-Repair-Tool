def sort_age(lst):
    if not lst:
        return []
    
    result = []
    for x in lst:
        inserted = False
        for i in range(len(result)):
            if x[1] > result[i][1]:
                result.insert(i, x)
                inserted = True
                break
        if not inserted:
            result.append(x)
    return result