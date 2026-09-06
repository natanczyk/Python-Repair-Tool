def sort_age(lst):
    # Create a copy of the list to avoid modifying the original input list
    people = list(lst)
    sort = []
    while people:
        oldest = people[0]
        for person in people:
            if person[1] > oldest[1]:
                oldest = person
        people.remove(oldest)
        sort.append(oldest)
    return sort