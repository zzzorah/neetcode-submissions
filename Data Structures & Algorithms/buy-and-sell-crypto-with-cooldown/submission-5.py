class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        cache = {}

        cache[length - 1] = 0
        for i in range(length - 2, -1, -1):
            result = cache[i + 1]
            for j in range(i + 1, length):
                diff = prices[j] - prices[i] if (prices[j] - prices[i]) > 0 else 0
                
                total = cache[j + 2] if j + 2 < length else 0
                result = max(result, diff + total)
            cache[i] = result

        return cache[0]
                    
