def sort_age(lst):
    old_lst = lst.copy()  # Create a copy to avoid modifying the original list
    new_lst = []
    while old_lst:
        largest = max(old_lst, key=lambda x: x[1])  # Find the tuple with the maximum age
        old_lst.remove(largest)
        new_lst.append(largest)
    return new_lst