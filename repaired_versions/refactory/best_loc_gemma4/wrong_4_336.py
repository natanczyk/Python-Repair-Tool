def sort_age(lst):
    if len(lst) <= 1:
        return lst
    else:
        # Find the index of the person with the maximum age
        max_age_index = 0
        for i in range(1, len(lst)):
            if lst[i][1] > lst[max_age_index][1]:
                max_age_index = i
        
        # Create a new list to avoid mutating the original list during recursion
        # and extract the oldest person
        remaining = lst[:]
        oldest = remaining.pop(max_age_index)
        
        return [oldest] + sort_age(remaining)