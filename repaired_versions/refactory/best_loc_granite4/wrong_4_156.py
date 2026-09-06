def sort_age(lst):
    new = []
    while lst:
        curr = lst[0]
        for i in lst:
            if i[1] > curr[1]:  # Find the maximum age
                curr = i
        lst.remove(curr)  # Remove the found maximum age element
        new.append(curr)  # Append the found maximum age element to the result
    return new