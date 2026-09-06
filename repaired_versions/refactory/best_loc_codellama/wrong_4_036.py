def sort_age(people):
    """selection sort"""
    for i in range(len(people)):
        max_age = people[i][1]
        max_index = i
        for j in range(i+1, len(people)):
            if people[j][1] > max_age:
                max_age = people[j][1]
                max_index = j
        people[i], people[max_index] = people[max_index], people[i]
    return people