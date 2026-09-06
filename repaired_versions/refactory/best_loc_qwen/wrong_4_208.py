def merge(one, two):
    new_tup = []
    while one and two:
        if one[0][1] > two[0][1]:  # Change the comparison to sort in descending order
            new_tup.append(one.pop(0))
        else:
            new_tup.append(two.pop(0))
    new_tup.extend(one)  # Append remaining elements from one
    new_tup.extend(two)  # Append remaining elements from two
    return new_tup

def sort_age(lst):
    n = len(lst)
    if n < 2:
        return lst
    left = lst[:n // 2]  # Use integer division
    right = lst[n // 2:]
    return merge(sort_age(left), sort_age(right))  # Recursively sort both halves before merging