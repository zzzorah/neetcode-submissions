class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        def heapify():
            i = (n - 2) // 2
            # print(f'n={n}')
            while i >= 0:
                j = 2*i + 1
                k = 2*i + 2
                # print(f'i={i}, j={j}, k={k}')
                # print(stones)

                if k < n:
                    if stones[j] > stones[i] and stones[j] >= stones[k]:
                        stones[j], stones[i] = stones[i], stones[j]
                    elif stones[k] > stones[i] and stones[k] >= stones[j]:
                        stones[k], stones[i] = stones[i], stones[k]
                elif stones[j] > stones[i]:
                    stones[j], stones[i] = stones[i], stones[j]

                i -= 1
        
        def getMax():
            nonlocal n 
            if n > 1:
                stones[0] = stones.pop()
                n -= 1
                if n > 2:
                    if stones[1] > stones[0] and stones[1] >= stones[2]:
                        stones[0], stones[1] = stones[1], stones[0]
                    elif stones[2] > stones[0] and stones[2] >= stones[1]:
                        stones[0], stones[2] = stones[2], stones[0]
                elif n > 1:
                    if stones[0] < stones[1]:
                        stones[0], stones[1] = stones[1], stones[0]
        
        heapify()
        print(stones)

        buffer = []

        while n > 1:
            buffer.append(stones[0])
            # print(f'{stones} n={n} buffer={buffer}')
            if len(buffer) == 2:
                diff = buffer[0] - buffer[1]
                if diff != 0:
                    stones.append(diff)
                    n += 1
                buffer = []

            getMax()
            # print(f'{stones} n={n}')
        
        if n == 0:
            return buffer[0] if len(buffer) != 0 else 0
        else: return stones[0]
                


