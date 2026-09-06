def sort_age(lst):
    sorted = []
    while lst:
        oldest = lst[0][1]
        for elem in lst:
            if elem[1] > oldest:
                oldest = elem[1]
        oldest_person = next(person for person in lst if person[1] == oldest)
        lst.remove(oldest_person)
        sorted.append(oldest_person)
    return sorted