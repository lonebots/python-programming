'''
Alice and Bob have an undirected graph of n nodes and three types of edges:

    Type 1: Can be traversed by Alice only.
    Type 2: Can be traversed by Bob only.
    Type 3: Can be traversed by both Alice and Bob.

Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:

Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

Example 2:

Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.

Example 3:

Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.


Constraints:

    1 <= n <= 105
    1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
    edges[i].length == 3
    1 <= typei <= 3
    1 <= ui < vi <= n
    All tuples (typei, ui, vi) are distinct.

'''

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # union find class 
        class UnionFind() :
            def __init__(self, n):
                self.representatives = list(range(n + 1))
                self.component_size = [1] * (n + 1)
                self.components = n 

            def find_representative(self, x): 
                if self.representatives[x] == x :
                    return x 
                self.representatives[x] = self.find_representative(self.representatives[x])
                return self.representatives[x]

            def perform_union(self, x, y):
                x = self.find_representative(x)
                y = self.find_representative(y) 

                if x == y: # already on the same disjoint set 
                    return 0 
                
                if self.component_size[x] > self.component_size[y] :
                    self.component_size[x] += self.component_size[y] 
                    self.representatives[y] = x 
                else : 
                    self.component_size[y] += self.component_size[x]
                    self.representatives[x] = y 
                
                # reduce number of components; since we combined 2 disjoint sets 
                self.components -= 1 
                return 1

            def is_connected(self):
                return self.components == 1 # only one single component
    
        # main logic 
        alice = UnionFind(n) 
        bob = UnionFind(n) 

        edges_required = 0

        # process edge type 3
        for edge in edges:
            if edge[0] == 3:
                v1 = edge[1]
                v2 = edge[2]
                edges_required += (alice.perform_union(v1, v2) | bob.perform_union(v1, v2))

        # process edge type 1 & 2
        for edge in edges:
            edge_type = edge[0]
            v1 = edge[1]
            v2 = edge[2]
            if edge_type == 2: # bob 
                edges_required += bob.perform_union(v1, v2)
            elif edge_type == 1: # alice 
                edges_required += alice.perform_union(v1, v2)

        # check if connected 
        if alice.is_connected() and bob.is_connected():
            return len(edges) - edges_required 

        return -1

