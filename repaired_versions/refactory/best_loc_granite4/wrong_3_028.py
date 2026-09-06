def remove_extras(lst):
    store = []
    for ele in lst:
        if ele not in store:
            store.append(ele)
    return store