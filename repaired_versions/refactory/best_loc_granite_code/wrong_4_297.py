def sort_age(lst):
    ages = []
    output = []
    for item in lst:
        ages.append(item[1])
    ages.sort(reverse=True)
    for age in ages:
        for item in lst:
            if age == item[1]:
                output.append(item)
    return output