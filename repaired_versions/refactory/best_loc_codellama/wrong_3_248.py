def remove_extras(lst):
    new_lst = []
    hashtable = {}
    for i in lst:
        if hashtable.get(i) != 1:
            hashtable[i] = 1
            new_lst.append(i)
    return new_lst