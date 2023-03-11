"""
problem : equl sum partition
aim     : to find out if we can partition the given array in two two subsets that have equal sum 

sample test case : 
    array   : [1,5,5,11] 
    output  : True

    solution : we can divide the array in to two parts [1,5,5] and [11] 

"""


def check(array):

    # test case
    sum_ = sum(array)
    n = len(array)
    target = -1
    if sum_ % 2 == 0:
        # division is possible
        target = sum_ // 2
    else:
        return False

    dp = [[None] * (target + 1) for _ in range(n + 1)]

    # initialization
    for r in range(n + 1):
        for c in range(target + 1):
            if r == 0:
                dp[r][c] = False
            if c == 0:
                dp[r][c] = True
    # print(dp)

    for r in range(n + 1):
        for c in range(target + 1):
            if array[r - 1] <= c:
                dp[r][c] = dp[r - 1][target - array[r - 1]] or dp[r - 1][c]
            else:
                dp[r][c] = dp[r - 1][c]

    return dp[n][target]


if __name__ == "__main__":
    # test case
    array1 = [1, 5, 5, 11]
    array2 = [2, 5, 5, 11]

    print("equal sum partition  : ", array1, check(array=array1))
    print("equal sum partition  : ", array2, check(array=array2))
