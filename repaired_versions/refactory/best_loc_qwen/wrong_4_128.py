def sort_age(lst):
    
    people = lst
    
    final = []
    
    while people:
        
        i = people[0]
        
        for a in people:
            
            if i[1] <= a[1] :
                
                i = a
                
        people.remove(i)
        final.append(i)
        
    return final