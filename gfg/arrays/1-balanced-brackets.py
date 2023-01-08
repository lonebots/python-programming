"""
Question : 
    write a program to find if the entered string satifies the condition of matching opening and closing brackets

    sample test cases 

    1. [[{}]]       -   YES
    2. [][]()       -   YES
    3. [(]          -   NO
    4. [(()]}       -   NO
    
 link to problem  : https://www.hackerrank.com/challenges/balanced-brackets/problem
 
"""


class solution:
    def isBalanced(self, s):
        pair = {"]": "[", ")": "(", "}": "{"}
        stck = []

        # check pair if only string is even length
        if len(s) % 2 == 0:  # check the opposite condition and return 'NO' - help reduce the loc
            for i in s:
                # left brackets push to stack
                if i in "([{":
                    stck.append(i)

                # right bracket with empty stack
                elif len(stck) == 0 and i in ")}]":
                    return "NO"

                # right bracket with elements in stack
                # elif len(stck) != 0 and i in ")]}" and pair[i] != stck.pop(): -- old
                elif i in ")]}" and pair[i] != stck.pop():  # -- new
                    return "NO"

            # after processing stack empty
            if len(stck) == 0:
                return "YES"
            else:
                return "NO"

        # odd length
        else:
            return "NO"


if __name__ == "__main__":
    s = input(">")  # take input string from user
    result = solution()
    print(f"result : ", result.isBalanced(s))
