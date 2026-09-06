def sort_age(lst):
    result = []
    for i in lst:
        result.append(i)
    result.sort(key=lambda x: x[1], reverse=True)
    return result