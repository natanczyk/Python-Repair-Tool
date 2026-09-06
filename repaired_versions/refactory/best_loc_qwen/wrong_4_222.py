def sort_age(lst):
    n = len(lst)
    result = []
    while n > 0:
        max_age = max([person[1] for person in lst])
        for i in range(n):
            if lst[i][1] == max_age:
                result.append(lst.pop(i))
                n -= 1
                break
    return result