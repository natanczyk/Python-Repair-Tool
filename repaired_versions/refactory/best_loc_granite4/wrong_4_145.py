def sort_age(lst):
    males, females = [], []
    for i in lst:
        if i[0] == "M":
            males.append(i)
        elif i[0] == "F":
            females.append(i)
    return merge(merge_sort(males), merge_sort(females))
    
def merge(left, right):
    results = []
    while left and right:
        # Compare by age (second element of tuple)
        if left[0][1] > right[0][1]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))
    results.extend(left)
    results.extend(right)
    return results

def merge_sort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)