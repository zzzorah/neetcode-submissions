class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        cache = {}

        if length == 1:
            return 0

        cache[length - 1] = 0
        if prices[length - 1] - prices[length - 2] > 0:
            cache[length - 2] = prices[length - 1] - prices[length - 2]
        else: cache[length - 2] = 0


        def dp(idx:int) -> int:
            if idx in cache:
                return cache[idx]

            result = dp(idx + 1)    # Don't buy on the ith day

            # Buy on the ith day, and j is the sell day
            if idx + 2 < length:
                for j in range(idx + 1, length):
                    total = 0
                    diff = prices[j] - prices[idx] if prices[j] - prices[idx] > 0 else 0
                    # print(f'i={idx}, j={j}, diff={diff}')

                    if (j + 2) < length:
                        total = dp(j + 2)
                        # for k in range(j + 2, length):
                        #     total = max(total, dp(k))
                    
                    result = max(diff + total, result)
                    # print(f'total={total}, result={result}')

            cache[idx] = result
            # print(cache, '\n')
            return result
        
        return dp(0)
                    
