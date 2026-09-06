def sort_age(lst):
    result = []
    for i in lst:
        for j in range(len(result)):
            if i[1] > result[j][1]:
                result.insert(j, i)
                break
        else:
            result.append(i)
    return result