class Solution:
    def hammingWeight(self, n: int) -> int:
        count_ = 0 
        while n :
            bit = n & 1 
            if bit == 1 :
                count_ += 1 
            n >>= 1

        return count_