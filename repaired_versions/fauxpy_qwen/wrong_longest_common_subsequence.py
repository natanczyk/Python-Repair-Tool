def longest_common_subsequence(a, b):
    if not a or not b:
        return ''

    elif a[0] == b[0]:
        return a[0] + longest_common_subsequence(a[1:], b[1:])

    else:
        subseq1 = longest_common_subsequence(a, b[1:])
        subseq2 = longest_common_subsequence(a[1:], b)
        return max(subseq1, subseq2, key=len)