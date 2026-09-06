def sort_age(lst):
    current=0
    tup=[]
    for i in lst:
        if i[1]>current:
            tup.insert(0,i)
            current=i[1]
        else:
            for j in range(len(tup)):
                if i[1]>tup[j][1]:
                    tup.insert(j,i)
                    break
                elif j==len(tup)-1:
                    tup.append(i)
    return tup