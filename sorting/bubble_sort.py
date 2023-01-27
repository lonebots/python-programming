'''
time complexity : O(n^2)
space complexity : O(1) - inplace sorting
'''


class solution:
    def bubble_sort(self, arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr


T = int(input())

for cases in range(T):
    # input
    arr = list(map(int, input("enter array").split()))

    result = solution()

    print(result.bubble_sort(arr))
