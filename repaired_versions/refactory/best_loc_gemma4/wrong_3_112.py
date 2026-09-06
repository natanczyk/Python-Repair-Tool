def remove_extras(lst):
    answer = []
    for i in lst:
        is_duplicate = False
        for a in answer:
            if i == a:
                is_duplicate = True
                break
        if not is_duplicate:
            answer.append(i)
    return answer