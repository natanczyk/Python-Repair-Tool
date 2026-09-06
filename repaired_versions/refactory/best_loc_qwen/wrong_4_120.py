def sort_age(lst):
    if not lst:
        return []
    
    result = []
    for x in lst:
        if not result or x[1] <= result[-1][1]:
            result.append(x)
        else:
            for i in range(len(result)):
                if x[1] > result[i][1]:
                    result.insert(i, x)
                    break
    
    return result