"""
Problem : 
    remove duplicate elements from a given integer array
    use inplace methods 

    return the no. of elements in the final list and print the list
"""


class solution:
    def __init__(self,nums) -> None:
        self.nums = nums
    
    def removeDuplicate(self, nums) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                
        return i+1  # always the index 1 less the length


if __name__ == "__main__":
    nums = list(map(int, input("array : ").split()))

    result = solution(nums)
    k = result.removeDuplicate(nums)
    print(f"result : ", result.nums[:k])
