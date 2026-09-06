def remove_extras(lst):
    answer = []
    for i in lst:
        if i not in answer:
            answer.append(i)
    return answer