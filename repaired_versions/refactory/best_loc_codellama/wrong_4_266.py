def sort_age(people):
    result = []
    while people:
        oldest = people[0]
        for person in people:
            if person[1] > oldest[1]:
                oldest = person
        result.append(oldest)
        people.remove(oldest)
    return result