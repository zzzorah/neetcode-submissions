class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        tmp = []
        for i in nums:
            for idx, value in enumerate(tmp):
                if value < i:
                    tmp.insert(idx, i)
                    break
            tmp.append(i)

        self.nums = tmp

    def add(self, val: int) -> int:
        for idx, value in enumerate(self.nums):
            if value < val:
                self.nums.insert(idx, val)
                break
        self.nums.append(val)
        
        return self.nums[self.k - 1]
