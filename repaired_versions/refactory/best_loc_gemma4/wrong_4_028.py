def sort_age(lst):
    def for_age(lst):
        for i in range(len(lst)):
            if i == 0: continue
            else:
                # Use a temporary variable for the inner loop index to avoid 
                # modifying the outer loop's iterator variable 'i'
                j = i
                while j > 0:
                    # Sort in descending order: swap if the current element 
                    # is older than the previous element
                    if lst[j][1] > lst[j-1][1]:
                        lst[j], lst[j-1] = lst[j-1], lst[j]
                        j -= 1
                    else: 
                        break
    for_age(lst)
    return lst