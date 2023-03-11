class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # brute force : TLE or WA incase of s = "ABBB" expected ans = 4 and result = 3 
        # max_length = 0
        # for left in range(len(s)) :
        #     change = k
        #     length = 0 
        #     right = left 
        #     while right < len(s) :
        #         if s[left] == s[right] :
        #             right += 1
        #             length += 1
                
        #         elif s[left] != right and change > 0  :
        #             change -= 1
        #             right += 1 
        #             length += 1
        #         else :
        #             break 
        #     max_length = max(max_length, length)
        # return max_length

        # approach 2 : sliding window 

        window_start  = 0 
        max_length = 0
        max_count = 0
        char_count = {}

        for window_end in range(len(s))  :
            # update the char count of char in window_end
            char_count[s[window_end]] = char_count.get(s[window_end],0) + 1

            # update max_count --> count of the maximum occuring character currently
            max_count = max(max_count, char_count[s[window_end]])

            # decrement the window size if required :
            if window_end - window_start + 1 > max_count + k :
                char_count[s[window_start]] -= 1
                window_start += 1 

            # update the maximum window size 
            max_length = max(max_length, window_end - window_start + 1)

        return max_length

            
                