def sort_age(lst):
    if not lst:
        return []
    
    max_age = lst[0][1]
    result = [lst[0]]
    
    for x in lst[1:]:
        if x[1] > max_age:
            result.insert(0, x)
            max_age = x[1]
        else:
            for i in range(len(result)):
                if x[1] > result[i][1]:
                    result.insert(i, x)
                    break
                elif i == len(result) - 1:
                    result.append(x)
    
    return result