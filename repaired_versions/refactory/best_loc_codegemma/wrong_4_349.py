def sort_age(lst):
    current=0
    tup=[]
    for i in lst:
        if i[1]>current:
            tup.append(i)
            current=i[1]
        else:
            tup.append(i)
    return sorted(tup, key=lambda x: x[1], reverse=True)