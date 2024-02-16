'''
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:

Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

 

Constraints:

    1 <= arr.length <= 10^5
    1 <= arr[i] <= 10^9
    0 <= k <= arr.length
'''

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Dictionary to track the frequencies of elements
        freq_map = Counter(arr)

        # List to track all the frequencies
        frequencies = list(freq_map.values())

        # Sorting the frequencies
        frequencies.sort()

        # Tracking the number of elements removed
        elements_removed = 0

        for i in range(len(frequencies)):
            # Removing frequencies[i] elements, which equates to
            # removing one unique element
            elements_removed += frequencies[i]

            # If the number of elements removed exceeds k, return
            # the remaining number of unique elements
            if elements_removed > k:
                return len(frequencies) - i

        # We have removed all elements, so no unique integers remain
        # Return 0 in this case
        return 0