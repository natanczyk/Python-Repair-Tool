def sort_age(lst):
    if not lst:  # Handle empty list
        return []
    if len(lst) == 1:
        return lst
    else:
        max_index = 0
        for i in range(1, len(lst)):
            if lst[i][1] > lst[max_index][1]:  # Find maximum age
                max_index = i
        return [lst[max_index]] + sort_age(lst[:max_index] + lst[max_index+1:])