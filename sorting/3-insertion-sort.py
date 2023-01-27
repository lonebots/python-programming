"""
consider sorted and unsorted list partitions
take an unsorted element, put it in the right place 
swap all the elements to the right and then make space for the correct element 

time complexity : O(n^2)
space complexity : O(1)
"""


class solution:
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > temp:
                arr[j + 1] = arr[j]

                # uncomment to visualise the sorting steps
                # arr[j] = 'x'
                # print(arr)

                j -= 1
            arr[j + 1] = temp
            
            # uncomment to visualise the sorting steps
            # print(arr)
        return arr


T = int(input())

for cases in range(T):
    # input
    arr = list(map(int, input().split()))

    result = solution()

    print(result.insertion_sort(arr))
