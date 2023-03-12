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
                cache[r][c] = 0
            if c == 0:
                cache[r][c] = 1

    for r in range(1, n + 1):
        for c in range(1, sum + 1):
            if arr[r - 1] <= c:
                cache[r][c] = cache[r - 1][c - arr[r - 1]] + cache[r - 1][c]
            else:
                cache[r][c] = cache[r - 1][c]

    return cache[n][sum]


if __name__ == "__main__":
    arr = [2, 2, 2, 2]
    diff = 0

    sum_ = (sum(arr) + diff)// 2

    print("no. of subsets with difference : ", diff, " ==> ", check(arr,sum_))
