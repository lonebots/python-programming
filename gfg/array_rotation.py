class solution:
    # left rotation
    def rotate_left(self, arr, k):
        mod = k % len(arr)
        return arr[mod:] + arr[:mod]

    # right rotation
    def rotate_right(self, arr, k):
        mod = len(arr) - (k % len(arr))
        return arr[mod:] + arr[:mod]


if __name__ == "__main__":
    arr = input("enter array : ").split()
    k = int(input("no. of times to be rotated : "))

    # implement class
    res = solution()

    right_rotated = res.rotate_right(arr, k)
    left_rotated = res.rotate_left(arr, k)

    # print result
    print(
        f"result \n left rotation : {left_rotated} \n right rotation : {right_rotated}"
    )
