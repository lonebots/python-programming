'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''

class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []

        # min heap ordered by character counts, so we will use 
        # negative values for count 
        pq = [(-count,char) for char,count in Counter(s).items()]
        heapify(pq)

        while pq : 
            count_first, char_first = heappop(pq)
            if not ans or char_first != ans[-1] :
                ans.append(char_first)
                if count_first + 1 != 0 :
                    heappush(pq,(count_first + 1,char_first))

            else :
                if not pq : return ""
                count_second, char_second = heappop(pq)
                ans.append(char_second)
                if count_second + 1 != 0 :
                    heappush(pq,(count_second +1,char_second ))
                heappush(pq, (count_first,char_first))

        return ''.join(ans)