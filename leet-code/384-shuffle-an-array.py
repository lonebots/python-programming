class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def reset(self) -> List[int]:
        return self.nums
        
    def shuffle(self) -> List[int]:
        shuffled = self.nums
        
        last = len(shuffled)-1 
        for i in range(len(shuffled)-1,-1,-1) :
            rand_ = randint(0,last)
            shuffled[rand_],shuffled[i] = shuffled[i],shuffled[rand_]
            last -= 1
        return shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()