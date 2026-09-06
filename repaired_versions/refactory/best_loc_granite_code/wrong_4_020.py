def sort_age(lst):
    new_lst = []
    for i in lst:
        for j in range(len(new_lst)):
            if i[1] > new_lst[j][1]:
                new_lst.insert(j, i)
                break
        else:
            new_lst.append(i)
    return new_lst