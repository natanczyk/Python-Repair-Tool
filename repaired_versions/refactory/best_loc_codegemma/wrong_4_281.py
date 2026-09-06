def sort_age(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j][1] < lst[j+1][1]:  # Fix comparison operator
                lst[j+1], lst[j] = lst[j], lst[j+1]  # Swap entire tuples
            else:
                continue
    return lst        
    pass