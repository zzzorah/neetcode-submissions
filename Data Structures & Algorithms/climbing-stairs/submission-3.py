class Solution:
    def climbStairs(self, n: int) -> int:
        max_two = n // 2
        total_count = 0

        for num_two in range(max_two + 1):
            num_one = n - 2 * num_two
            total = num_one + num_two
            diff = min(num_one, num_two)

            count = 1
            for j in range(total, total - diff, -1):
                count *= j
            
            if diff != 0:
                for j in range(diff, 0, -1):
                    count /= j

            total_count += count
            # if num_one > num_two:
            #     count = 1
            #     for j in range(total, num_one - 1, -1):
            #         if j != 0:
            #             count *= j
            #     for j in range(1, num_two + 1):
            #         if j != 0:
            #             count /= j
            #     total_count += count
            # else:
            #     count = 1
            #     for j in range(total, num_two - 1, -1):
            #         if j != 0:
            #             count *= j
            #     for j in range(1, num_one + 1):
            #         if j != 0:
            #             count /= j
            #     total_count += count
        
        return int(total_count)