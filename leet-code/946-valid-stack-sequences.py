'''
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

 

Constraints:

    1 <= pushed.length <= 1000
    0 <= pushed[i] <= 1000
    All the elements of pushed are unique.
    popped.length == pushed.length
    popped is a permutation of pushed.

'''

'''
Approach : 
    * push elements in order of pushed to a stack :
    * keep a variable to count the pop index 
    * pop elements if stack top matchs with the popped element index 
    * if element is popped then increment the index variable by 1 
    * return the result true if index == len(total popped elements list) else return false result.
'''


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        idx = 0 

        for n in pushed :
            stack.append(n)
            while stack and idx < len(popped) and stack[-1] == popped[idx] :
                stack.pop()
                idx += 1
        
        return idx == len(popped)