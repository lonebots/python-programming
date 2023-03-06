class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
 # optiized dynamic programming solution 

        # dp = [False] * (len(s) + 1)
        # dp [len(s)] = True  
        # for i in range(len(s) - 1, -1, -1) :
        #     for w in wordDict : 
        #         if i + len(w) <= len(s) and s[i:i +len(w)] == w :
        #             dp[i] = dp[i + len(w)] 
        #         if dp[i] :
        #             break
        # return dp[0]  

# brute force : recurssion  --> TLE

        # def dfs (idx) :
        #     if idx == len(s) :
        #         return True

        #     for end in range(idx+1,len(s)+1) :
        #         if s[idx:end]  in wordDict and dfs(end) :
        #             return True
        #     return False
        # return dfs(0)

# recurssion with memorization -- > AC
        # @lru_cache()
        # def wordbreakMemo (idx) :
        #     if idx == len(s) :
        #         return True
        #     for end in range(idx + 1, len(s) + 1) :
        #         if s[idx:end] in wordDict and wordbreakMemo(end) :
        #             return True
        #     return False

        # return wordbreakMemo(0)

# breadth first search -- > 
        q = []
        visited = set()
        word_set = set(wordDict) 

        q.append(0)
        while q : 
            start = q.pop(0)
            if start in visited :
                continue
            for end in range(start+1,len(s)+1) :
                if s[start:end] in word_set :
                    q.append(end) 
                    if end == len(s) :
                        return True
            visited.add(start)
        return False