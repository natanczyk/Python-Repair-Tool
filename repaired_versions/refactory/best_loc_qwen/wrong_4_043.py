def sort_age(lst):
    if not lst:
        return []
    
    result = [lst[0]]
    for i in lst[1:]:
        inserted = False
        for j in range(len(result)):
            if i[1] >= result[j][1]:
                result.insert(j, i)
                inserted = True
                break
        if not inserted:
            result.append(i)
    return result