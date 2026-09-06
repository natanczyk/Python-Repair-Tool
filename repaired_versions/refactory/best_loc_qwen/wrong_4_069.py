def sort_age(lst):
    store = []
    for i in lst:
        if len(store) == 0:
            store.append(i)
        else:
            for j in range(len(store)):
                if i[1] > store[j][1]:
                    store.insert(j, i)
                    break
            else:
                store.append(i)
    return store