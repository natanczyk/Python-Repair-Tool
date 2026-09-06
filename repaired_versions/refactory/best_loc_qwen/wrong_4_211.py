def sort_age(lst):
    n = len(lst)
    result = []
    while n > 0:
        max_age = max(lst, key=lambda x: x[1])[1]
        for counter in range(n):
            if lst[counter][1] == max_age:
                result.append(lst.pop(counter))
                break
        n = len(lst)
    return result