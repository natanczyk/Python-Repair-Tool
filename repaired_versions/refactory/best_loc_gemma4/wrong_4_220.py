def sort_age(lst):
  # The goal is to sort the people such that the older people are at the front.
  # The tuples are in the format (gender, age).
  # We need to sort by the second element of the tuple (age) in descending order.
  return sorted(lst, key=lambda x: x[1], reverse=True)