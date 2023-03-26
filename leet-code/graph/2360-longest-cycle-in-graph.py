'''
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.

 

Example 1:

Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.

Example 2:

Input: edges = [2,-1,3,1]
Output: -1
Explanation: There are no cycles in this graph.

 

Constraints:

    n == edges.length
    2 <= n <= 105
    -1 <= edges[i] < n
    edges[i] != i
'''

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        #functional graph 
        n = len(edges) 

        visited = [False] * n 
        maxDist = -1

        def visit(node) :
            dist = 0
            previous = {}

            while not visited[node] :
                visited[node] = True
                previous[node] = dist
                dist += 1
                if edges[node] != -1 :
                    node = edges[node]
                    if node in previous : # a cycle found
                        nonlocal maxDist
                        maxDist = max( maxDist, dist - previous[node]) 
                        return 

        for node in range(n) :
            if not visited[node] and edges[node] != -1  :
                visit(node)

        return maxDist



# failed attempt --> TLE 63/76
        # # create a adjacency list.
        # adj_list = { }

        # for node in range(len(edges)) :
        #     adj_list[node] = edges[node]

        # def dfs (start, node,count) :
        #     # check if it forms a cycle
        #     # increment count if one node gets added

        #     if cycle and node == cycle[0] :
        #         return count

        #     if node == -1 or node in cycle :
        #         return -1 

        #     count += 1
        #     cycle.append(node)
        #     node = adj_list[node]
        #     return dfs(cycle, node,count)

        # res = -1
        # for node in range(len(edges)) :
        #     cycle = []
        #     count = 0
        #     res = max(res, dfs(cycle,node,count))
            
        # return res 
        