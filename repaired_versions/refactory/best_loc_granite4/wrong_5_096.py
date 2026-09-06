def top_k(lst, k):
    # Implementing a simple selection sort to sort the list in descending order
    for i in range(len(lst)):
        # Find the index of the maximum element in the remaining unsorted portion
        max_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[max_index]:
                max_index = j
        # Swap the found maximum element with the first element of the unsorted portion
        lst[i], lst[max_index] = lst[max_index], lst[i]
    
    # Return the top k elements
    return lst[:k]