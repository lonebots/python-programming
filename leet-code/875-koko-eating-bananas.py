import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # helper funcition
        def canEatAllBananaWithSpeed( speed ) :
            eating_time = 0 # in hours
            for pile in piles :
                eating_time += math.ceil(pile/speed)  # updated time for completely eating each pile
            
            return eating_time <= h 

        # binary search 
        left = 1   # minimum number of bananas that koko can eat
        right = max(piles)  # maximum number of banans that koko may eat

        while left < right :
            mid = (left + right ) // 2   # mid value --> rate or the speed at which koko choose to eat
            if canEatAllBananaWithSpeed(mid) :
                right = mid 
            else :
                left = mid + 1 

        return left 