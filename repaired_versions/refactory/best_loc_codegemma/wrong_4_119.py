def sort_age(lst):
    if not lst:
        return []
    result = [lst[0]]
    for x in lst[1:]:
        for i in range(len(result)):
            if x[1] > result[i][1]:
                result.insert(i, x)
                break
            elif i == len(result) - 1:
                result.append(x)
    return result