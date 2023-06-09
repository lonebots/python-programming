'''
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.


There can be duplicate entries in the array of letters. 
'''

# solution 1 

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters = sorted(set(letters))
        left, right = 0, len(letters)-1
        while left <= right :
            mid = (left + right) // 2 
            if ord(letters[mid]) == ord (target) :
                return letters[mid+1] if mid + 1 < len(letters) else letters[0]
            elif ord(letters[mid]) < ord(target) :
                left = mid + 1 
            else :
                right = mid - 1 
        return letters[left] if left < len(letters) else letters[0]


# solution 2 

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=0
        r=len(letters)
        while l<r:
            mid= l + (r - l) // 2
            if letters[mid]<=target:
                l=mid+1
            else:
                r=mid
        return letters[l%len(letters)]
