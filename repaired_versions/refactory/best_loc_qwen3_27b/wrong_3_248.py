def remove_extras(lst):
    newLst=[]
    hashtable={}
    for i in lst:
        if hashtable.get(i, 0) != 1:
            hashtable[i]=1
            newLst.append(i)
            
        
    return newLst