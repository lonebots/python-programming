"""
based on DIVIDE AND CONQUER METHOD

We can choose where ever the pivot element can be 
1. starting 
2. ending 
3. random
4. median

time complexity :   
    1. worst case --> array already sorted --> O(n^2)
    2. average case --> O(nlogn)
    3. best case --> (going for the median element as the pivot each time ) pivot dividing array half each time --> O(nlogn) 

space complexity : constant --> O(1)

"""


class solution:
    def quickSort(self, arr):
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] == arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def sort_array(arr, low, high):
            if low <= high:
                pi = partition(arr=arr, low=low, high=high)

                sort_array(arr=arr, low=low, high=pi - 1)
                sort_array(arr=arr, low=pi + 1, high=high)

            return arr

        return sort_array(arr, 0, len(arr) - 1)


def main(args=None):
    result = solution()

    t1 = [1, 2, 3, 4, 5]
    t2 = [5, 3, 1, 2, 4]

    print("result 1 : ", result.quickSort(t1))
    print("result 2 : ", result.quickSort(t2))


if __name__ == "__main__":
    main()
