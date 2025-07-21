"""
This problem was asked by Google.

The edit distance between two strings
refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other.
For example,
    the edit distance between “kitten” and “sitting” is three:
    substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

# class WordHandler:
#     def __init__(self):
#         pass

#     @staticmethod
#     def compute_distance(word1: str, word2: str) -> int:
#         index1 = index2 = 0

#         return WordHandler.edit(index1, index2)

#     @staticmethod
#     def edit(index1: int, index2: int) -> int:
#         pass


def compute_distance(word1: str, word2: str) -> int:
    def edit(index1, index2) -> int:
        if index1 >= len(word1):  # base case 1: exhaust word1
            return len(word2) - index2

        if index2 >= len(word2):  # base case 2: exhause word2
            return len(word1) - index1

        if word1[index1] == word2[index2]:
            return edit(index1 + 1, index2 + 1)  # no cost
        else:
            return 1 + min(
                edit(index1, index2 + 1),  # insert
                edit(index1 + 1, index2),  # delete
                edit(index1 + 1, index2 + 1),  # substituion
            )  # cost of this operation and min of future operations

    return edit(0, 0)


def compute_distance_with_memoization(word1: str, word2: str) -> int:
    len_word1 = len(word1)
    len_word2 = len(word2)
    dp = [[None] * (len_word2 + 1) for _ in range(len_word1 + 1)]

    def edit(index1, index2) -> int:
        # memoize
        if dp[index1][index2] is not None:
            return dp[index1][index2]

        if index1 >= len(word1):  # base case 1: exhaust word1
            dp[index1][index2] = len(word2) - index2
            return dp[index1][index2]

        if index2 >= len(word2):  # base case 2: exhause word2
            dp[index1][index2] = len(word1) - index1
            return dp[index1][index2]

        if word1[index1] == word2[index2]:
            return edit(index1 + 1, index2 + 1)  # no cost
        else:
            dp[index1][index2] = 1 + min(
                edit(index1, index2 + 1),  # insert
                edit(index1 + 1, index2),  # delete
                edit(index1 + 1, index2 + 1),  # substituion
            )  # cost of this operation and min of future operations
            return dp[index1][index2]

    return edit(0, 0)


if __name__ == "__main__":
    word1: str = "kitten"
    word2: str = "sitting"

    result = compute_distance(word1=word1, word2=word2)
    result_memoized = compute_distance_with_memoization(word1=word1, word2=word2)

    print(result)
    print(result_memoized)
