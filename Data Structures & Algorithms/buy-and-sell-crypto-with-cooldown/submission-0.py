class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        cache = {}

        cache[length - 1] = 0
        cache[length - 2] = prices[length - 1] - prices[length - 2] if prices[length - 1] - prices[length - 2] > 0 else 0

        def dp(idx:int) -> int:
            if idx in cache:
                return cache[idx]

            result = 0
            for j in range(idx + 1, length):
                diff = prices[j] - prices[idx] if prices[j] - prices[idx] > 0 else 0
                result = max(result, prices[j] - prices[idx] + max(dp(k) for k in range(j + 2, length)))
            cache[idx] = result
            return result
        
        return dp(0)
                    
