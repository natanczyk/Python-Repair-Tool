def sort_age(lst):
    output = []
    while lst:
        smallest = lst[0]
        for i in lst:
            if i[1] > smallest[1]:  # Change comparison to find the largest age
                smallest = i
        lst.remove(smallest)  # Remove the smallest element
        output.append(smallest)  # Append the smallest element to the output list
    return output