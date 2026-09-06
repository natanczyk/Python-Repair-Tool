def sort_age(lst):
    if len(lst) <= 1:  # Handle both empty list and single element list
        return lst
    max_age = max(lst, key=lambda x: x[1])[1]
    max_person = next(person for person in lst if person[1] == max_age)
    remaining = [person for person in lst if person != max_person]
    return [max_person] + sort_age(remaining)