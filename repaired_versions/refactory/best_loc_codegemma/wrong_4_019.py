def sort_age(lst):
    product = []
    while lst:
        smallest = lst[0]
        for i in lst:
            if i[1] > smallest[1]:  # Fix: Change `<` to `>` for descending order
                smallest = i
        lst.remove(smallest)
        product.append(smallest)
    return product