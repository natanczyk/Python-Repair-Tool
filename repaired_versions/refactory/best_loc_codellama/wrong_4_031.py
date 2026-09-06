def sort_age(people):
    if len(people) == 0:
        return []
    elif len(people) == 1:
        return people
    else:
        mid = len(people) // 2
        lst1 = sort_age(people[:mid])
        lst2 = sort_age(people[mid:])
        
        result = []
        while lst1 and lst2:
            if lst1[0][1] < lst2[0][1]:
                result.append(lst2.pop(0))
            else:
                result.append(lst1.pop(0))
        result.extend(lst1)
        result.extend(lst2)
        
        return result