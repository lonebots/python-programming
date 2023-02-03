class Solution:
    def fib(self, n: int) -> int:
        # iterative solution 
        fib = [0,1]  # first and second fib
        for i in range(2,n+1) :
            fib.append(fib[i-1] + fib[i-2])

        return fib[n]