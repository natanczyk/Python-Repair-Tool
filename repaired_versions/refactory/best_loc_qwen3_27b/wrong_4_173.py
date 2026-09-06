def sort_age(lst):
    sort = []
    while lst:
        # Find the tuple with the largest age
        largest = lst[0]
        for i in range(len(lst)):
            if lst[i][1] > largest[1]:
                largest = lst[i]
        # Remove the largest tuple from the original list
        lst.remove(largest)
        # Append the full tuple to the sorted list
        sort.append(largest)
    return sort