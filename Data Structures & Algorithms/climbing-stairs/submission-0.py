class Solution:
    def climbStairs(self, n: int) -> int:
        max_two = n // 2
        total_count = 0

        for num_two in range(max_two):
            num_one = n - 2 * num_two
            total = num_one + num_two

            if num_one > num_two:
                count = 1
                for j in range(total, num_one - 1, -1):
                    count *= j
                for j in range(1, num_two + 1):
                    count /= j
                total_count += count
        
        return total_count