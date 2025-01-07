'''
Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string

 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 30
    words[i] contains only lowercase English letters.
    All the strings of words are unique.
'''


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = lambda word : len(word))

        result = []
        for i in range(len(words)):
            curr_word = words[i]

            for j in range(i+1, len(words)):
                word = words[j]

                if curr_word in word and curr_word not in result:
                    result.append(curr_word)
                
            
        return result
    
    
# optimized solution 
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        r=' '.join(words)
        s=[i for i in words if r.count(i)>1]
        return s