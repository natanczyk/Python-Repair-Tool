def top_k(lst, k):
    counter=0
    new_lst=[]
    while counter<k and lst:
        new_lst.append(lst.pop(lst.index(max(lst))))
        counter+=1
    return new_lst