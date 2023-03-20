'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids :
            '''
            1. negative asteroid can stay in the bottom of the stack
            2. postive astroids coming after that will not interact with the bottom most negative astroids
            3. negative asteroid coming after the postive will interact
            '''
            while stack and stack[-1] > 0 and asteroid < 0 :
                if stack[-1] == -asteroid : # equal size 
                    stack.pop()
                    break
                
                elif stack[-1] > -asteroid :
                    break
                
                elif stack[-1] < -asteroid :
                    stack.pop()
                    continue
            else :
                stack.append(asteroid) 
        return stack 
        


# failed attempt 

# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         stack = []  # (direction, size)
#         for ast in asteroids :
#             direct = 1 if ast > 0 else -1 
#             ast = abs(ast)
#             print("direct : ",direct,"ast :",ast) 
#             if stack and stack[-1][1] == ast and stack[-1][0] != direct :
#                 stack.pop()
#                 continue
            
#             while stack and stack[-1][0] != direct :
#                 c_direct, c_ast = stack.pop()
#                 direct = c_direct if c_ast > ast else direct
#                 ast = max(ast,c_direct) 
            
#             stack.append((direct,ast))  
#         res = []
#         for direct, ast in stack :
#             res.append(direct*ast)
            
#         return res