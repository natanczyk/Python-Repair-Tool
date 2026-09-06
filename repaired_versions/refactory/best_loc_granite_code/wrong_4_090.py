def sort_age(lst):
    if lst == []:
        return []
    max_person = max(lst, key=lambda x: x[1])
    return [max_person] + sort_age([person for person in lst if person != max_person])