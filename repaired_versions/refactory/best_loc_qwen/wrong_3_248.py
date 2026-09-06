def remove_extras(lst):
    newLst = []
    hashtable = {}
    for i in lst:
        if i not in hashtable:
            hashtable[i] = 1
            newLst.append(i)
    
    return newLst