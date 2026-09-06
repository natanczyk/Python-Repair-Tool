def sort_age(lst):
    answer = []
    while lst:
        biggest = lst[0]
        for person in lst:
            if person[1] > biggest[1]:
                biggest = person
        answer.append(biggest)
        lst.remove(biggest)
    return answer