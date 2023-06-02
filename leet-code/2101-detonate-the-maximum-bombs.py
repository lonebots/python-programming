''' 
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
Example 1:

Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.

'''

class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        n = len(bombs)

        # build the graph
        for i in range(n) :
            for j in range(n) :
                if i == j :
                    continue 
                xi, yi, ri = bombs[i]
                xj, yj, _  = bombs[j]

                # create a path from node i to j if bomb i detonates bomb j 
                if ri ** 2 >= ( xi - xj) ** 2 + (yi - yj) ** 2 :
                    graph[i].append(j)

        # do dfs
        def dfs( curr, visited) :
            visited.add(curr)
            for neighbor in graph[curr] :
                if neighbor not in visited :
                    dfs(neighbor,visited)
            return len(visited)

        answer = 0 
        for i in range(n) :
            visited = set()
            answer = max(answer, dfs(i,visited))
        return answer