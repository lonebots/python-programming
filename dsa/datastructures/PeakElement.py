"""
Question : Given an array arr[] of integers. Find a peak element i.e. an element that is not smaller than its neighbors. 

edge cases : 
    1. strictly increasing list, then last element is peak elemnt.
    2. strictly decreasing list, then first element is the peak element.
    3. array with all elements same, then all elements are peak element.

 * naive approach : 
    looping and searching each element's left and right to satify below condition
        arr[i-1] < arr[i] and arr[i+1] > arr[i]

        time complexity     : O(n)
        space complexity    : O(1)
 
 * recursive binary search : 
    set mid = (low + high) // 2
    updated call >> low = mid + 1 if arr[mid+1] > arr[mid]
    updated call >> high = mid - 1 if arr[mid-1] > arr[mid]

        time complexity     : O(logn)
        space complexity    : O(logn)

 * iterative binary search
    set mid = (low + high) // 2
    updated call >> low = mid + 1 if arr[mid+1] > arr[mid]
    updated call >> high = mid - 1 if arr[mid-1] > arr[mid]

        time complexity     : O(logn)
        space complexity    : O(1)

    SIMILAR PROBLEMS 
        1. LOCAL MINIMA
        2. ?


SOLUTION : 
"""


class solution:
    def findPeak(self, arr):
        # iterative binary search
        l = 0  # left pointer
        r = len(arr) - 1  # right pointer
        while l <= r:
            mid = (l + r) // 2  # set mid
            if (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]) and (
                mid == 0 or arr[mid] > arr[mid - 1]
            ):
                return arr[mid]
            if arr[mid - 1] > arr[mid]:
                r = mid - 1
            elif arr[mid + 1] > arr[mid]:
                l = mid + 1
        return -1


if __name__ == "__main__":
    arr = list(map(int, input(">").split()))
    result = solution()
    print(f"peak element in {arr} : ", result.findPeak(arr))
