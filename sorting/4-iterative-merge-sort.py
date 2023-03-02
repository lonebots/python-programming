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

    return sorted_list  # merged sorted list


# bottom up approach = YES
# varible to tell where we are in the merging process


def loop(arr):
    size = 1  #  min size of individual arrays
    n = len(arr)
    while size < n:
        low = 0

        # a loop to merge the pair of arrays
        while low < n - 1:
            # calculate the mid and high
            mid = min(low + size - 1, n - 1)
            high = min(low + size * 2 - 1, n - 1)

            # merge the sub arrays
            merge(arr[low:mid], arr[mid + 1: high])

            low += size * 2
        size *= 2

    return arr


arr = [1, 3, 2, 5, 2, 0, 10]

print(loop(arr))
