# Problem: 121. Best Time to Buy and Sell Stock
#
# Approach:
# - Use two nested loops to check every possible buy day and sell day.
# - Calculate the profit for each pair where the sell day comes after the buy day.
# - Keep track of the maximum profit found.
# - Return the maximum profit at the end.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        return profit
