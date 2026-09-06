def sort_age(lst):
    def age(i):
        return i[1]
    
    def largest_age(seq):
        largest = seq[0]
        for item in seq:
            if age(item) > age(largest):
                largest = item
        return largest
    
    if not lst:
        return []
    if len(lst) == 1:
        return lst
    
    max_item = largest_age(lst)
    max_index = lst.index(max_item)
    return [max_item] + sort_age(lst[:max_index] + lst[max_index+1:])