class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                tmp_profit = price - min_price
                if profit < tmp_profit:
                    profit = tmp_profit
        
        return profit