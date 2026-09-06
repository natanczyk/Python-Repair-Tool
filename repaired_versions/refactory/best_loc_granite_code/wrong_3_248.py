def remove_extras(lst):
    new_lst = []
    hashtable = {}
    for i in lst:
        if i not in hashtable:
            hashtable[i] = 1
            new_lst.append(i)
    return new_lst