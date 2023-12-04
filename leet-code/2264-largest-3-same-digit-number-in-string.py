'''
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

    It is a substring of num with length 3.
    It consists of only one unique digit.

Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

    A substring is a contiguous sequence of characters within a string.
    There may be leading zeroes in num or a good integer.

 

Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".

Example 2:

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.

Example 3:

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

 

Constraints:

    3 <= num.length <= 1000
    num only consists of digits.

'''

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Assign 'max_digit' to NUL character (smallest ASCII value character)
        max_digit = '\0'

        # Iterate on characters of the num string.
        for index in range(len(num) - 2):
            # If 3 consecutive characters are the same,
            # store the character in 'max_digit' if it's bigger than what it already stores.
            if num[index] == num[index + 1] == num[index + 2]:
                max_digit = max(max_digit, num[index])

        # If 'max_digit' is NUL, return an empty string; otherwise, return a string of size 3 with 'max_digit' characters.
        return '' if max_digit == '\0' else max_digit * 3