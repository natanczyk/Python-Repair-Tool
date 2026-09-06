def sort_age(lst):
    for i in range(len(lst)):
        max_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j][1] > lst[max_idx][1]:  # Find the maximum age from i to the end
                max_idx = j
        lst[i], lst[max_idx] = lst[max_idx], lst[i]  # Swap the found maximum with lst[i]
    return lst