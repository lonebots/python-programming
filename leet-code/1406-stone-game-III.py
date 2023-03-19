"""
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.

The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.

 

Example 1:

Input: values = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.

Example 2:

Input: values = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.

"""


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        # approach 1 : recurrsive solution --> TLE
        # approach 2 : memoisation --> dp - top down
        # appraoch 3 : dp --> bottom up

        cache = [-1] * (len(stoneValue) + 1)

        def calculate_score(i, s):
            if i == len(s):
                return 0
            if cache[i] != -1:
                return cache[i]
            else:
                max_ = float("-inf")
                max_ = max(s[i] - calculate_score(i + 1, s), max_)
                if i + 1 < len(s):
                    max_ = max(max_, s[i] + s[i + 1] - calculate_score(i + 2, s))
                if i + 2 < len(s):
                    max_ = max(
                        max_, s[i] + s[i + 1] + s[i + 2] - calculate_score(i + 3, s)
                    )

                cache[i] = max_
                return cache[i]

        alice = calculate_score(i=0, s=stoneValue)

        if alice > 0:
            return "Alice"
        elif alice == 0:
            return "Tie"
        else:
            return "Bob"


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        # approach 1 : recurrsive solution --> TLE
        # approach 2 : memoisation
        n = len(stoneValue)
        cache = [-1] * (n + 1)

        def calculate_score(i, s):
            if i == n:
                return 0
            if cache[i] != -1:
                return cache[i]
            else:
                max_ = float("-inf")

                max_ = max(
                    max_,
                    s[i] - calculate_score(i + 1, s),
                    s[i] + s[i + 1] - calculate_score(i + 2, s) if i + 1 < n else 0,
                    s[i] + s[i + 1] + s[i + 2] - calculate_score(i + 3, s)
                    if i + 2 < n
                    else 0,
                )

                cache[i] = max_
                return cache[i]

        alice = calculate_score(i=0, s=stoneValue)

        if alice > 0:
            return "Alice"
        elif alice == 0:
            return "Tie"
        else:
            return "Bob"
