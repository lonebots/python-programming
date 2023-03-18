'''
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

    BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
    void visit(string url) Visits url from the current page. It clears up all the forward history.
    string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
    string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

 
'''

# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.history = [homepage]
#         self.curr = 0
        
#     def visit(self, url: str) -> None:
#         if self.curr == len(self.history) - 1 :
#             self.curr += 1
#             self.history.append(url)
#         else :
#             self.history = self.history[:self.curr+1] + [url]
        
#     def back(self, steps: int) -> str:
#         if self.curr - steps  < 0 :
#             self.curr = 0
#         else :
#             self.curr -= steps
#         return self.history[self.curr]
        
#     def forward(self, steps: int) -> str:
#         if self.curr + steps < len(self.history) :
#             self.curr += steps
#         else :
#             self.curr = len(self.history) - 1 
#         return self.history[self.curr]
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr] = url
        self.bound = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.bound)
        return self.history[self.curr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)