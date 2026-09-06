def sort_age(lst):
    # The problem asks to sort by age in descending order.
    # Python's sorted() and list.sort() are stable, meaning they preserve 
    # the original relative order of elements that have the same key.
    # Based on the test cases, a simple descending sort by age is required.
    return sorted(lst, key=lambda x: x[1], reverse=True)