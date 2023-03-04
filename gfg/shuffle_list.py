import random
class solution :
    def shuffle_list(self,nums) :
        n = len(nums)
        for idx in range(n) :
            r = random.randint(idx,n-1) 
            nums[r],nums[idx] = nums[idx], nums[r]
        return nums

if __name__ == "__main__" :
    nums = list(map(int,input().split()))

    res = solution()
    print(res.shuffle_list(nums))
