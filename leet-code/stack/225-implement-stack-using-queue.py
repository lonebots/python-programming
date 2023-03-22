'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

    You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
    Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

'''
import collections
class MyStack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())
        
    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]
    
    def empty(self):
        return not len(self._queue)
# class MyStack:

#     def __init__(self):
#         self.q1 = []
#         self.q2 = []
#         self.top = None
         
#     def push(self, x: int) -> None:
#         self.q1.append(x)
#         self.top = x
    
#     def pop(self) -> int:
#         if len(self.q1) > 0 :
#             while len(self.q1) > 1 :
#                 self.q2.append(self.q1.pop(0))
        
#         popelement = self.q1.pop(0)
#         while self.q2 :
#             if len(self.q2) == 1 :
#                 self.top = self.q2[0]
#             self.q1.append(self.q2.pop(0))
        
#         return popelement

#     def top(self) -> int:
#         return self.top

#     def empty(self) -> bool:
#         return len(self.q1) == 0
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()