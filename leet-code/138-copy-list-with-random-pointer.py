'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        head_list = []
        visited = {}
        counter = 0
        while head:
            head_list.append(head)
            visited[head] = counter
            counter +=1
            head = head.next
            
        ans = Node(0, None, None)
        ans_list = []
        for x in head_list:
            ans.val, ans.next = x.val, Node(0, None, None)
            ans_list.append(ans)
            ans = ans.next
            
        ans_list[-1].next = None
        ans = ans_list[0]
        
        for i, x in enumerate(head_list):
            if x.random:
                ans_list[i].random = ans_list[visited[x.random]]
                #print(visited[x.random])
                #print(ans_list[visited[x.random]])
                
        return ans_list[0]



        # if not head :
        #     return head 

        # visited = {}
        # head_list = []
        # counter = 0

        # while head :
        #     head_list.append(head)
        #     visited[head] = counter 
        #     counter += 1
        #     head = head.next

        # answer = Node(0,None,None)
        # answer_list = []
        # for node in head_list :
        #     answer.val, answer.next = node.val, Node(0,None,None)
        #     answer_list.append(answer)
        #     answer = answer.next

        # answer_list[-1].next = None    
        # answer = answer_list[0]

        # for idx, node in enumerate(answer_list) :
        #     if node.random :
        #         answer_list[idx].random = head_list[visited[node.random]]

        # return answer_list[0]
