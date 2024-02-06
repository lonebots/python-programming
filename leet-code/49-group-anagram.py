'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.


'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = dict()
        answers = []

        for word in strs :
            nword = ''.join(sorted(list(word)))
            if nword in dict_ :
                dict_[nword].append(word)
            else :
                dict_[nword] = [word]

        # for key in dict_.keys() :
        #     answers.append(dict_[key])

        # return answers
        return dict_.values()