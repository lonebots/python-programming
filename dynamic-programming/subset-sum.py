"""
AIM : to find if a subset exist in the given integer array that sum up to the target sum that we have given

test case 1 :
    arr = [1,2,3,4,5]
    target_sum = 8 

    output : True 
    solution : [3,5] sums up to 8 
"""

# implementation 1
def recurssive_check(n, sum):
    if n == 0:
        # print("sum : ",sum)
        if sum == 0:
            return True
        else:
            return False

    if arr[n - 1] <= sum:
        return recurssive_check(n - 1, sum - arr[n - 1]) or recurssive_check(n - 1, sum)

    else:
        return recurssive_check(n - 1, sum)


# implementation 2
def memoisation_check(n, sum):
    # helper function
    def helper(n, sum):
        if n == 0:
            if sum == 0:
                return cache[n][sum]
            else:
                return cache[n][sum]

        if cache[n][sum]:
            return cache[n][sum]

        if arr[n - 1] <= sum:
            cache[n][sum] = helper(n - 1, sum - arr[n - 1]) or helper(n - 1, sum)
            return cache[n][sum]

        else:
            cache[n][sum] = helper(n - 1, sum)
            return cache[n][sum]

    # driver code
    cache = [[None] * (sum + 1) for _ in range(n + 1)]
    for r in range(n + 1):
        for c in range(sum + 1):
            if r == 0:
                cache[r][c] = False
            if c == 0:
                cache[r][c] = True
    return helper(n, sum)


# implementation 3 : bottom up dp
def dp_check(n, sum):
    dp = [[None] * (sum + 1) for _ in range(n + 1)]
    for r in range(n + 1):
        for c in range(sum + 1):
            if r == 0:
                dp[r][c] = False
            if c == 0:
                dp[r][c] = True

    for r in range(1, n + 1):
        for c in range(1, sum + 1):
            if arr[r - 1] <= c:
                dp[r][c] = dp[r - 1][c - arr[r - 1]] or dp[r - 1][c]
            else:
                dp[r][c] = dp[r - 1][c]
    return dp[n][sum]

# main
if __name__ == "__main__":
    arr = [1, 10, 12, 4, 5]
    sum = 1

    n = len(arr)

    print("subset sum - recurrsion  : ", recurssive_check(n, sum))
    print("subset sum - memoisation : ", memoisation_check(n, sum))
    print("subset sum - bottomup    : ", dp_check(n, sum))
