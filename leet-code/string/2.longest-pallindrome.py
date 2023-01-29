class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)
    

# or 

class Solution:
    def longestPalindrome(self, s: str) -> int:

        if len(s) == 1 :
            return 1 

        max_len_pallindrome = 0 
        hashMap = {}
        for i in s :
            if i not in hashMap.keys() :
                hashMap[i] = 1
            else :
                hashMap[i] += 1
        
        
        flag = 0 

        for i in hashMap.keys() :
            
            if hashMap[i] % 2 == 0 :
                max_len_pallindrome += hashMap[i] 
            else:
                max_len_pallindrome += hashMap[i] // 2 *2 
                flag = 1

        if flag == 1 :
            return max_len_pallindrome + 1 
        else :
            return max_len_pallindrome
        
