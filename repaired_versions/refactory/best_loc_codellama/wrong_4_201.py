def sort_age(people):
    sorted_people = []
    for person in people:
        if len(sorted_people) == 0:
            sorted_people.append(person)
        else:
            for i in range(len(sorted_people)):
                if person[1] > sorted_people[i][1]:
                    sorted_people.insert(i, person)
                    break
            else:
                sorted_people.append(person)
    return sorted_people