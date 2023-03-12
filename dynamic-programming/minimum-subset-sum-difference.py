"""
problem : To minimise the difference between two subsets of a given array.

test case       :
    array       : [1,2,3,,7]
    output      : 1
    solution    : s1 = [1,2,3] and s2 = [7] their difference is 1  
"""


def check(arr, sum):
    n = len(arr)

    cache = [[None] * (sum + 1) for _ in range(n + 1)]
    for r in range(n + 1):
        for c in range(sum + 1):
            if r == 0:
                cache[r][c] = False
            if c == 0:
                cache[r][c] = True

    for r in range(1, n + 1):
        for c in range(1, sum + 1):
            if arr[r - 1] <= c:
                cache[r][c] = cache[r - 1][c - arr[r - 1]] or cache[r - 1][c]
            else:
                cache[r][c] = cache[r - 1][c]

    return cache[n][sum]


if __name__ == "__main__":
    arr = [1, 2, 3, 7]

    min_ssum = float("inf")

    start = 0
    total = sum(arr)
    end = total // 2

    for sum in range(start, end + 1):
        if check(arr, sum):
            min_ssum = min(min_ssum, total - (2 * sum))


    print("mininum subset difference : ",min_ssum)