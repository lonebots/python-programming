# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 0,n
        while l <= r:
            m = (l+r)//2
            #print(guess(m))
            if guess(m) == 0 :
                return m
            elif guess(m) == 1:
                l = m +1
            elif guess(m) == -1:
                r = m
        
        