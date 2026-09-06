def sort_age(lst):
    holder = []
    for x in lst:
        if holder == []:
            holder = [x]
        elif x[1] > holder[0][1]:
            holder = [x] + holder
        else:
            i = 0
            while i < len(holder) and holder[i][1] > x[1]:
                i += 1
            holder.insert(i, x)
    return holder