def longest_common_subsequence(a, b):
    if not a or not b:
        return ''

    elif a[0] == b[0]:
        return a[0] + longest_common_subsequence(a[1:], b[1:])

    else:
        sub1 = longest_common_subsequence(a, b[1:])
        sub2 = longest_common_subsequence(a[1:], b)
        return sub1 if len(sub1) >= len(sub2) else sub2