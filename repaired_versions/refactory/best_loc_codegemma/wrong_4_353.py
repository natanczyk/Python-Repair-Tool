def sort_age(lst):
    # Fill in your code here
    A = sorted(lst, key=lambda x:x[1], reverse=True)
    return A