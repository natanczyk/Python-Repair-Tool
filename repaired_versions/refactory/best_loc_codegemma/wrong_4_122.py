def sort_age(lst):
    if not lst:
        return []
    result = lst[:]
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i][1] < result[j][1]:
                result[i], result[j] = result[j], result[i]
    return result