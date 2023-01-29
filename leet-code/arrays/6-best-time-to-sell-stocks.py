class Solution:
    def maxProfit(self, prices) -> int:

        # approach 1 : brute force (TLE)
        # max_profit = 0
        # for i in range(len(prices)) :
        #     for j in range(i+1,len(prices)) :
        #         if prices[j] - prices[i] > max_profit :
        #             max_profit = prices[j] - prices[i]

        # return max_profit

        # # approach 2 - One pass
        max_profit = 0
        min_price = float("inf")

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit


def main(args=None):
    result = Solution()

    prices = list(map(int, input(" Enter stock price list : ").split()))

    print("max profit : ", result.maxProfit(prices))
