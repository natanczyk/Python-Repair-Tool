def sort(lst):
    # Bubble sort implementation for descending order by age (index 1)
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j][1] < lst[j + 1][1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def sort_age(lst):
    # Create a copy to avoid modifying the original list if needed, 
    # but since we return the sorted list, we can sort in place or return new
    # The problem asks to return a sorted list. Let's sort a copy to be safe.
    result = list(lst)
    sort(result)
    return result