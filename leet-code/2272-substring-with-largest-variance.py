'''
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.
Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.
A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.
Example 2:

Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''

'''
solution approach :
********** modified kadane's algorithm ************
'''

class Solution:
    def largestVariance(self, s: str) -> int:
        counter = [0] * 26

        # count the total occurance of each letter in the string
        for ch in s :
            counter[ord(ch)-ord('a')] += 1 
        
        global_max = 0
        for i in range(26) :
            for j in range(26) :
                # donot do anything
                if i == j or counter[i] == 0 or counter[j] == 0 :
                    continue
                
                # set major and minor character
                major = chr(ord('a')+i)
                minor = chr(ord('a')+j)
                
                # initialize variables to track their count
                major_count = 0 
                minor_count = 0

                # set the rest with minor's count
                rest_minor = counter[j]
        
                # loop and update the values - main loop (updated Kadane's' algorithm)
                for ch in s :
                    if ch == major : 
                        major_count += 1
                    
                    if ch == minor : 
                        minor_count += 1
                        rest_minor -= 1

                    # update variance ( local_max ) if there is atleast 1 minor
                    if minor_count > 0 :
                        global_max = max(global_max, major_count - minor_count)

                    # discard the previous string (set all counts = 0) if we have atleast 1 remaining minor
                    if (major_count < minor_count and rest_minor > 0 ) :
                        major_count = 0
                        minor_count = 0
        return global_max