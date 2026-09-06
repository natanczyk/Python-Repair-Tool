def sort_age(lst):
    new = []
    while lst:
        curr = lst[0]
        for i in lst:
            if i[1] > curr[1]:  # Change comparison to descending order
                curr = i
        lst.remove(curr)  # Remove the target element
        new.append(curr)  # Append the target element
        
    return new