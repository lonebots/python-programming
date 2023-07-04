'''
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
 

Constraints:

1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters.
'''

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # length comparision
        if len(s) != len(goal) :
            return False

        # both are equal then there should be an item to swap
        freq = [0] * 26 # to store the frequency of each letter
        if s == goal :
            for ch in s:
                freq[ord(ch)-ord('a')] += 1
                if freq[ord(ch)-ord('a')] == 2 :
                    return True
            # otherwise nothing to swap
            return False

        # we need atleast 2 indices with different characters, so that we can swap
        firstIndex = secondIndex = -1
        for i in range(len(s)) :
            if s[i] != goal[i] :
                if firstIndex == -1 :
                    firstIndex = i
                elif secondIndex == -1 :
                    secondIndex = i
                else : 
                    # we have more than two characters to swap 
                    #which is not posssible according the question's conditions.
                    return False
        # no second index; means no element to swap
        if secondIndex == -1 :
            return False 
        
        # Check all character with goal and return results
        return s[firstIndex] == goal[secondIndex] and s[secondIndex] == goal[firstIndex] 