def remove_extras(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Alternative recursive version that fully removes extras:
# def remove_extras(lst):
#     for i in set(lst):
#         while lst.count(i) > 1:
#             lst.remove(i)
#     return lst