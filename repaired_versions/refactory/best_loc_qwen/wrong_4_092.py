def sort_age(lst):
    answer = []
    while lst:
        biggest = lst[0]
        for a in range(len(lst)):
            if lst[a][1] > biggest[1]:
                biggest = lst[a]
        answer.append(biggest)
        lst.remove(biggest)
    return answer