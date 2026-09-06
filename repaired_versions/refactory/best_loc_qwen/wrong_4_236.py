def sort_age(lst):
    def age(i):
        return i[1]
        
    def position(seq, ele):
        n = len(seq)
        for i in range(n):
            if seq[i] == ele:
                return i
                
    def largest_age(seq):
        largest = age(seq[0])
        largest_pos = 0
        for i in range(len(seq)):
            if age(seq[i]) > largest:
                largest = age(seq[i])
                largest_pos = i
        return seq[largest_pos]
    
    n = len(lst)
    if n <= 1:
        return lst
    else:
        largest = largest_age(lst)
        lst.remove(largest)
        return [largest] + sort_age(lst)