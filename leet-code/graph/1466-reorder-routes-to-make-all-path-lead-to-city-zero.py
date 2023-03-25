'''
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

 

Example 1:

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

'''

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        edges = {(a,b) for a,b in connections}
        neighbours = { city : [] for city in range (n)}
        changes = 0

        # populate neighbours
        for a , b in connections :
            neighbours[a].append(b)
            neighbours[b].append(a)

        visited = set()
        # dfs and check if neighbour can reach city 0
        def dfs(city) :
            nonlocal changes,neighbours, edges, visited
            for neighbour in neighbours[city] :
                if neighbour in visited :
                    continue 
                
                visited.add(neighbour)

                if (neighbour, city) not in edges :
                    changes += 1

                dfs(neighbour)

        visited.add(0) # make city 0 to be visited
        dfs(0)

        return changes
   
# failed attempt   
        # self.count = 0 

        # adj = [set()] * n # adjacency list : --> adj[a] => [(b,0) or (b,1)] : 1 -> original 0 -> artificial

        # # create the adj list 
        # for a,b in connections :
        #     adj[a].add((b,1))
        #     adj[b].add((a,0)) 

        # print(adj)
        # visited = set()
        # def dfs(parent,node) :
        #     if node == n - 1 :
        #         return 
        #     for child,sign in adj[node] :
        #         if child != parent and child not in visited:
        #             visited.add(child)
        #             self.count += 1 if sign == 0 else 0
        #             dfs(parent = node,node = child)

        # # call dfs
        # dfs(0,0)

        # return self.count 

        