def sort_age(lst):
    s = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        smallest = temp_lst[0]
        for element in temp_lst:
            if element[1] < smallest[1]:
                smallest = element
        temp_lst.remove(smallest)
        s.append(smallest)
    
    # Reverse the list once at the end to get descending order (older people first)
    s.reverse()
    return s