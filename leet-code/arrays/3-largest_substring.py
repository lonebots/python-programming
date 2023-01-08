from re import sub
from typing import SupportsIndex


def lengthOfLongestSubstring(s: str) -> int:
    max_substring_length = 0
    for i in range (len(s)) : 
        j = i 
        substring = ""
        while j < len(s) and s[j] not in substring :          
            substring += s[j]
            j += 1
        if (len(substring) > max_substring_length) :
            max_len_ss = substring
            max_substring_length = len(substring) 
    return max_substring_length


s = "jbpnbwwd"

print(lengthOfLongestSubstring(s))
