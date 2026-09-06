def sort_age(lst):
    new = []
    while lst:
        curr = lst[0][1]
        counter = 0
        for i in range(len(lst)):
            if lst[i][1] > curr:  # Find the maximum age
                curr = lst[i][1]
                counter = i
        new.append(lst[counter])  # Append the tuple, not the index
        lst.pop(counter)  # Remove the tuple by index
    return new