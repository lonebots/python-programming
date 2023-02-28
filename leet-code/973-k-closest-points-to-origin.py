import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def find_dist(x,y) :
            return round(math.sqrt((x*x + y*y)),2)
        
        dist = []
        for idx, coord in enumerate(points) :
            x, y = coord
            dist.append((idx,find_dist(x,y)))
        
        print(dist)
        dist.sort(key = lambda item : item[1]) 

        res = []
        for i in range(k) :
            res.append(points[dist[i][0]])
        
        return res