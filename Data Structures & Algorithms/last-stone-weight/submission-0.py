class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        result = 0
        for s in stones:
            if result == 0:
                result = s
            else:
                result = abs(result - s)

        return result