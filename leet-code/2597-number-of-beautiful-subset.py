'''
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].

 

Constraints:

    1 <= nums.length <= 20
    1 <= nums[i], k <= 1000

'''

class Solution:
    def beautifulSubsets(self, nums: List[int], k) -> int:
        total_count = 1
        freq_map = defaultdict(lambda: defaultdict(int))

        # Calculate frequencies based on remainder
        for x in nums:
            freq_map[x % k][x] += 1

        # Calculate subsets for each remainder group
        for fr in freq_map.values():
            s = sorted(fr.items())
            counts = [-1] * len(s)  # Store counts of subsets for memoization
            total_count *= self._count_beautiful_subsets(s, k, 0, counts)

        return total_count - 1  # Subtract 1 for the empty subset

    def _count_beautiful_subsets(
        self, subsets: List[List[int]], difference: int, i: int, counts: List[int]
    ) -> int:
        # Base case: Return 1 for a subset of size 1
        if i == len(subsets):
            return 1

        # If the count is already calculated, return it
        if counts[i] != -1:
            return counts[i]

        # Calculate subsets where the current subset is not taken
        skip = self._count_beautiful_subsets(subsets, difference, i + 1, counts)

        # Calculate subsets where the current subset is taken
        take = (1 << subsets[i][1]) - 1

        # If the next number has a difference of 'difference',
        # calculate subsets accordingly
        if i + 1 < len(subsets) and subsets[i + 1][0] - subsets[i][0] == difference:
            take *= self._count_beautiful_subsets(subsets, difference, i + 2, counts)
        else:
            take *= self._count_beautiful_subsets(subsets, difference, i + 1, counts)

        counts[i] = skip + take  # Store and return total count of subsets
        return counts[i]