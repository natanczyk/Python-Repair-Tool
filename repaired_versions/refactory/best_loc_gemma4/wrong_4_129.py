def sort_age(lst):
    
    people = []
    
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    
    while temp_lst:
        
        i = temp_lst[0]
        
        for a in temp_lst:
            
            if a[1] >= i[1]:
                
                i = a
                
        temp_lst.remove(i)
        
        people.append(i)
        
    return people