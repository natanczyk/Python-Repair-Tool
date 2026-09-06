def subsequences(a, b, k):
    if k == 0:
        return [[]]

    ret = []
    for i in range(a, b - k + 1):  # ensure enough numbers left to pick k-1 more
        ret.extend(
            [i] + rest for rest in subsequences(i + 1, b, k - 1)
        )

    return ret