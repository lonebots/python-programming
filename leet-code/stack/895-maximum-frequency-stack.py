'''
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

    FreqStack() constructs an empty frequency stack.
    void push(int val) pushes an integer val onto the top of the stack.
    int pop() removes and returns the most frequent element in the stack.
        If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
'''

class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.maxCnt = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        valCnt = 1 + self.cnt.get(val,0)
        self.cnt[val] = valCnt
        if valCnt > self.maxCnt :
            self.maxCnt = valCnt
            self.stacks[valCnt] = []
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] -=1 
        if not self.stacks[self.maxCnt] :
            self.maxCnt -= 1

        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()