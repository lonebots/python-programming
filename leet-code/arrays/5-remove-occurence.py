"""
Problem : 
    remove all the occurances of an elements from a given integer array
    use inplace methods 

    return the no. of elements in the final list and print the list

    **APPROACH 
        Two pointer method
"""


class solution:
    def __init__(self, nums) -> None:
        self.nums = nums

    def removeDuplicate(self, nums, val) -> int:
        i = 0
        for j in range(len(nums)):
            if self.nums[j] != val:
                self.nums[i] = nums[j]
                i += 1
        return i  # always the index 1 less the length


if __name__ == "__main__":
    nums = list(map(int, input("array : ").split()))
    val = int(input("to be removed : "))

    result = solution(nums)
    k = result.removeDuplicate(nums, val)
    print(f"result : ", result.nums[:k])
