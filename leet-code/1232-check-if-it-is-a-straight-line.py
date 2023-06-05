# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        # assign first two points
        (x1,y1),(x2,y2) = coordinates[:2]  

        # use line equation 
        for i in range(2,len(coordinates)) :
            x, y = coordinates[i] 
            #  check line equation 
            if (y2 - y1) * (x - x2) != (y - y2) * (x2 - x1) :
                return False 
        return True