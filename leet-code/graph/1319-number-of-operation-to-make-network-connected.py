'''
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.

'''

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # edge case : check if no. of present connection is sufficient to reconnect the system to make it fully connected
        if len(connections) < n - 1:
            return -1

        # get the count of number of connected components 

        graph = [ set() for _ in range(n)] 

        # prepare a graph out of the connection
        for a,b in connections :
            graph[a].add(b)
            graph[b].add(a)

        visited = [0 ] * n # keep a count of visited nodes

        # to find a connected component
        def dfs (node) :
            if visited[node] :
                return 0 
            else :
                visited[node] = 1
                for neighbour in graph[node] :
                    dfs(neighbour)
                return 1
            
        # get all connected components 
        components = 0
        for node in range(n) :
            components += dfs(node)

        return components - 1


        

        