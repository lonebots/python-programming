class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province_count  = 0 
        visited = set()

        def dfs (neighbourcities) :
            for neighbour, connected in enumerate (neighbourcities) :
                if connected and neighbour not in visited :
                    visited.add(neighbour) 
                    dfs(isConnected[neighbour])

        # travel through all the cities and do a dfs 
        for city, neighbourcities in enumerate(isConnected) :
            if city not in visited :
                dfs(neighbourcities)
                province_count += 1  
        return province_count 