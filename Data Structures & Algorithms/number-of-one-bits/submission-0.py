class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        count = 0
        while n > 1:
            rem = n % 2
            if rem == 1:
                count += 1
                print(count, n)
            
            n = (n - rem) / 2
        
        if n == 1:
            count += 1

        return count

            
