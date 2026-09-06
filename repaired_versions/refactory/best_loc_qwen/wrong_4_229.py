def sort_age(lst):
    if not lst:
        return lst
    
    for i in range(len(lst)):
        youngest_index = i
        for j in range(i+1, len(lst)):
            if lst[j][1] > lst[youngest_index][1]:
                youngest_index = j
        lst[i], lst[youngest_index] = lst[youngest_index], lst[i]
    
    return lst