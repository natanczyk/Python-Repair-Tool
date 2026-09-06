def sort_age(lst):
    final = []
    while lst:
        smallest = lst[0]
        for i in lst:
            if i[1] > smallest[1]:  # Fix comparison to find the largest age
                smallest = i
        lst.remove(smallest)
        final.append(smallest)
    return final  # Return the final list instead of printing it