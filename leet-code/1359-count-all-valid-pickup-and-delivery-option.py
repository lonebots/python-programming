''' 
Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
Example 3:

Input: n = 3
Output: 90
 

Constraints:

1 <= n <= 500
'''

class Solution:
    def __init__(self) :
        self.MOD = int(1e9 + 7) # modulus
        self.memoization = []   # memoisation array to store values
    
    def calculateOrdersCount(self, remainingPairs) :
        # base case
        if remainingPairs == 0 :
            return 1

        # check if the value is already computed and then return it 
        if self.memoization[remainingPairs] != -1 :
            return self.memoization[remainingPairs]

        # calculate the number of valid orders for the remaining pairs 
        currentResult = self.calculateOrdersCount(remainingPairs - 1) * ( 2 * remainingPairs - 1) * remainingPairs % self.MOD

        # store the result in memoization array and return it 
        self.memoization[remainingPairs] = currentResult
        return self.memoization[remainingPairs]

    def countOrders(self, numPairs: int) -> int:
        # initialisation
        self.memoization = [-1] * (numPairs + 1)

        # calculate and return
        return self.calculateOrdersCount(numPairs)
