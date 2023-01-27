"""
- Recursive method
works with the divide an conquer technique
divide the array in to n sublist 
sort the individual arrays 
merge them to form final single sublist

time complexity : O(nlogn)
"""


class solution:
    def do_merge_sort(self, arr):
        def merge(left, right):
            l_index, r_index = 0, 0
            sorted_list = []
            while l_index < len(left) and r_index < len(right):
                if left[l_index] < right[r_index]:
                    sorted_list.append(left[l_index])
                    l_index += 1
                else:
                    sorted_list.append(right[r_index])
                    r_index += 1 

            sorted_list += left[l_index:]
            sorted_list += right[r_index:]

            return sorted_list # merged sorted list 
        
        def merge_sort(arr):
            pass
            # base case
            if len(arr) <= 1:
                return arr

            # divide and merge
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left=left, right=right)
        
        # call the fucntion 
        return merge_sort(arr=arr)


def main(args=None):
    arr = list(map(int, input("enter array > ").split()))

    result = solution()

    print("sorted array > ", result.do_merge_sort(arr))


if __name__ == "__main__":
    main()
