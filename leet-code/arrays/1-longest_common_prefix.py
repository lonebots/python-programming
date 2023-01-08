'''
PROBLEM :
    find the longest prefix string from a list of string, else return an empty string ""

    Eg 1 : 
        strs = ['flower', 'flow','floor']
        result = 'flo'

    Eg 2 :
        strs = ['cat','dog','rat']
        result = ""

SOLUTION :
    
'''


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s = ""
        for i in range(len(min(strs))):
            lettertocheck = min(strs)[i]
            for j in strs:
                if j[i] != lettertocheck:
                    return s
            s += lettertocheck
        return s


if __name__ == "__main__":
    strs = input("list of strings : ").split()

    result = Solution()

    print("Longest Common Prefix : ", result.longestCommonPrefix(strs=strs))
