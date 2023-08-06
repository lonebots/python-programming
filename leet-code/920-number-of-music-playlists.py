'''
Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

Every song is played at least once.
A song can only be played again only if k other songs have been played.
Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, goal = 3, k = 1
Output: 6
Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
Example 2:

Input: n = 2, goal = 3, k = 0
Output: 6
Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
Example 3:

Input: n = 2, goal = 3, k = 1
Output: 2
Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].
'''

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 1_000_000_007
        dp = [[-1 for _ in range(n + 1)] for _ in range(goal + 1)] 
        
        def number_of_playlists(i,j) : 
            # base case 
            if i == 0 and j == 0 :
                return 1 

            if i == 0 or j == 0 :
                return 0 
            
            if dp[i][j] != -1 :
                return dp[i][j]

            # transition : add new song or replay an old song 
            dp[i][j] = (number_of_playlists(i-1,j-1) *(n-j+1)) % MOD

            if j > k :
                dp[i][j] += (number_of_playlists(i-1,j) *(j-k)) % MOD
                dp[i][j] %= MOD
            return dp[i][j]
            
        return number_of_playlists(goal,n)