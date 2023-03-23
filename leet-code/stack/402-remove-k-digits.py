'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

 

Constraints:

    1 <= k <= num.length <= 105
    num consists of only digits.
    num does not have any leading zeros except for the zero itself.

'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num :  
            while k > 0 and stack and stack[-1] > n :
                k -= 1
                stack.pop()
            stack.append(n)

        stack = stack[:len(stack)-k]  # k might still be not 0
        
        res = "".join(stack)
        return str(int(res)) if res else "0"


# failed attempt

# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         n = len(num)
#         k_ = k
#         stack = [] 
#         idx = 0
#         if len(num) <= k :
#             return '0'
#         while idx < len(num) and k > 0 :

#             if stack and stack[-1] < num[idx] :
#                 k -= 1
#                 idx += 1
#                 continue
            
#             while stack and stack[-1] > num[idx] and k > 0 :
#                     k -= 1
#                     stack.pop()

#             stack.append(num[idx])   

#             idx += 1

#         print("stack --> ",stack)

#         num = str(int(''.join(stack) + num[idx:]))
#         return num[:n-k_]
