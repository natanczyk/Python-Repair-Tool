def sort_age(lst):
    output = []
    while lst:
        smallest = lst[0]
        for i in lst:
            if i[1] > smallest[1]:  # Change from < to >
                smallest = i
        lst.remove(smallest)  # Corrected to remove the smallest element
        output.append(smallest)  # Append the smallest element instead of i
    return output