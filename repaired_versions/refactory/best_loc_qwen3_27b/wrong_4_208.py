def merge(one, two):
    new_tup = []
    while one and two:
        # Sort in descending order by age (older people first)
        if one[0][1] > two[0][1]:
            new_tup.append(one.pop(0))
        else:
            new_tup.append(two.pop(0))
    # Append remaining elements from either list
    new_tup.extend(one)
    new_tup.extend(two)
    return new_tup

def sort_age(lst):
    n = len(lst)
    if n < 2:
        return lst
    # Use integer division for slicing
    mid = n // 2
    left = sort_age(lst[:mid])
    right = sort_age(lst[mid:])
    return merge(left, right)