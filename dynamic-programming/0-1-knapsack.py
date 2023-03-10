"""
AIM : we have to maximise the value / profit by adding elements to the knapsack such that their agregate weight doesn't exceed W
"""
weight = [1, 2, 5, 7]
value = [1, 10, 2, 6]
W = 7

dp = [[-1] * (W + 1) for _ in range(len(value) + 1)]
for i in range(len(value) + 1):
    for j in range(W + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0

# print(dp)


def recurssive_knapsack(n, w):

    # base condtion
    if n == 0 or w == 0:
        return 0

    # choise diagram
    if weight[n - 1] <= w:
        return max(
            value[n - 1] + recurssive_knapsack(n - 1, w - weight[n - 1]),
            recurssive_knapsack(n - 1, w),
        )  # when weight[n] < w we have two options
    else:
        return recurssive_knapsack(n - 1, w)


def memoization_knapsack(n, w):
    if n == 0 or w == 0:
        return dp[n][w]

    # USE FROM THE CACHE
    if dp[n][w] != -1:
        return dp[n][w]

    if weight[n - 1] <= w:
        dp[n][w] = max(
            value[n - 1] + memoization_knapsack(n - 1, w - weight[n - 1]),
            memoization_knapsack(n - 1, w),
        )
        return dp[n][w]
    else:
        dp[n][w] = memoization_knapsack(n - 1, w)
        return dp[n][w]


def bottom_up_knapsack(n, w):
    cache = [[-1] * (w + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
    # cache
    # print("INITIAL - CACHE --> ",cache)
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if weight[i - 1] <= j:
                cache[i][j] = max(
                    value[i - 1] + cache[i - 1][j - weight[i - 1]], cache[i - 1][j]
                )
            else:
                cache[i][j] = cache[i - 1][j]
        
    # print("FINAL - CACHE --> ",cache)
    return cache[n][w]


if __name__ == "__main__":

    n = len(value)  # index of the last element in weight array / value array
    w = W  # initial weight when no items present
    # recurssive knapsack call
    print("max_profit - recurssion  : ", recurssive_knapsack(n, w))

    # memoization knapsack call
    print("max_profit - memo        : ", memoization_knapsack(n, w))

    # bottom up dynamic programming 
    print("max_profit - bottom up   : ", bottom_up_knapsack(n,w))
