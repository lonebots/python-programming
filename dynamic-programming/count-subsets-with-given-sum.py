"""
problem : find the number of subsets with a given sum

test case : 
    array       : [11,2,3,4,5,8,10]
    sum         : 10
    output      : 3 
    solution    : subsets that add up to 10 are [2,3,5], [2,8], [10] 
"""

# recurssive solution implementation 
def reccursive_count_subsets(array,sum) :
    n = len(array) 

    # helper function
    def helper (n,sum) :
        if n == 0 :
            if  sum == 0 :
                return 1
            else :
                return 0
            
        if array[n-1] <= sum :
            return helper(n-1,sum-array[n-1]) + helper(n-1,sum) 
    
        else :
            return helper(n-1,sum)
    
    return helper(n,sum)

# dynamic programming implementation 
def count_subsets(array, sum):
    n = len(array)

    # cache
    cache = [[-1] * (sum + 1) for _ in range(n + 1)]

    for r in range(n + 1):
        for c in range(sum + 1):
            if r == 0:
                cache[r][c] = 0
            if c == 0:
                cache[r][c] = 1

    for r in range(1, n + 1):
        for c in range(1, sum + 1):
            if array[r - 1] <= c:
                cache[r][c] = cache[r - 1][c - array[r - 1]] + cache[r - 1][c]
            else:
                cache[r][c] = cache[r - 1][c]

    return cache[n][sum]


if __name__ == "__main__":
    array = [11, 2, 3, 4, 5, 8, 10]
    sum = 10

    print('subset sum count             : ',count_subsets(array,sum))
    print('subset sum count recurssive  : ',reccursive_count_subsets(array,sum))
