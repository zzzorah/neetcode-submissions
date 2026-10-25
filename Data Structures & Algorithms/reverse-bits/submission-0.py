class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(31, -1, -1):
            k = 31 - i

            result += ((n >> i) & 1) * 2**k

        return result