class Solution:
    def isHappy(self, n: int) -> bool:
        stack = set()

        while n != 1:
            sum = 0
            while True:
                if n // 10 == 0:
                    sum += n ** 2
                    break   
                else:
                    sum += (n % 10) ** 2
                    n = n // 10

            if sum in stack:
                return False
            
            stack.add(sum)
            n = sum

        return True