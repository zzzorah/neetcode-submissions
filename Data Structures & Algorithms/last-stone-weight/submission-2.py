class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        def heapify():
            i = (n - 2) // 2
            while i > 0:
                j = 2*i + 1
                k = 2*i + 2
                
                if stones[j] > stones[k] and stones[j] > stones[i]:
                    stones[j], stones[i] = stones[i], stones[j]
                elif stones[k] > stones[j] and stones[k] > stones[i]:
                    stones[k], stones[i] = stones[i], stones[k]
                i += 1
        
        def getMax():
            nonlocal n 
            if n > 1:
                stones[0] = stones.pop()
                n -= 1
                if n > 2:
                    if stones[1] > stones[0] and stones[1] > stones[2]:
                        stones[0], stones[1] = stones[1], stones[0]
                    elif stones[2] > stones[0] and stones[2] > stones[1]:
                        stones[0], stones[2] = stones[2], stones[0]
                elif n > 1:
                    if stones[0] < stones[1]:
                        stones[0], stones[1] = stones[1], stones[0]
        
        heapify()
        buffer = []

        while n > 0:
            buffer.append(stones[0])

            if len(buffer) == 2:
                diff = buffer[0] - buffer[1]
                if diff != 0:
                    stones.append(diff)
                    n += 1
                buffer = []

            getMax()
        
        if n == 0:
            return buffer[0] if len(buffer) != 0 else 0
        else: return stones[0]
                


