def merge(one, two):
    new_tup = []
    while one and two:
        if one[0][1] > two[0][1]:  # sort in descending order
            new_tup.append(one.pop(0))
        else:
            new_tup.append(two.pop(0))
    new_tup.extend(one)  # append remaining elements from one
    new_tup.extend(two)  # append remaining elements from two
    return new_tup

def sort_age(lst):
    n = len(lst)
    if n < 2:
        return lst
    left = lst[:n // 2]  # use integer division
    right = lst[n // 2:]
    return merge(sort_age(left), sort_age(right))  # recursive calls added