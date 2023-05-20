'''
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

    There are no self-edges (graph[u] does not contain u).
    There are no parallel edges (graph[u] does not contain duplicate values).
    If v is in graph[u], then u is in graph[v] (the graph is undirected).
    The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

 

Example 1:

Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Example 2:
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
'''
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        ''' plan :
             * do a bfs 
             * mark a color for each node currently visiting ( either 0 or 1)
             * make sure that no adjacent color are same 
        '''
        n = len(graph)
        color = [-1] * n 

        for i in range(n) :
            if color[i] != -1 :
                continue

            q = deque()
            q.append((i,0))  # start with each node and color 0

            # bfs
            while q : 
                node, col = q.popleft()
                # color is not assigned
                if color[node] == -1 :
                    color[node] = col
                    for nx in graph[node] :
                        q.append((nx,col^1)) # xor toggles between 0 and 1
                    
                # already a color is assigned
                if color[node] != col :
                    return False

        return True