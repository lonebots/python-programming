class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # range base binary search 
        min_time = min(time)
        left = 1 
        right = totalTrips * min_time

        while left < right :
            mid_time = (left + right) // 2 
            trip_completed = 0 
            for t in time :
                trip_completed += mid_time // t

            if trip_completed < totalTrips :
                left = mid_time + 1

            else :
                right = mid_time 

        return left