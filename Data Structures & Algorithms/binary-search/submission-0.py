class Solution:
    def search(self, nums: List[int], target: int) -> int:
        target_idx = -1
        idx = -1
        def divide(nums: List[int]):
            nonlocal target_idx, idx
            
            if len(nums) == 1:
                idx += 1
                if nums[0] == target:
                    target_idx = idx
            else:
                divide(nums[:len(nums)//2])
                if target_idx == -1:
                    divide(nums[len(nums)//2:])

        divide(nums)
        return target_idx