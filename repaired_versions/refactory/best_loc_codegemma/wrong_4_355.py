def sort_age(lst):
    # Fill in your code here
    newlst=[]
    while lst:
        maximum = lst[0][1]
        maxi = lst[0]
        for i in lst:
            if i[1]>maximum:
                maximum = i[1]
                maxi = i
        newlst.append(maxi)
        lst.remove(maxi)

    return newlst