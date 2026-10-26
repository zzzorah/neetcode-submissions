class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        def divide(s_idx:int, e_idx:int):
            if s_idx == e_idx and target != nums[s_idx]:
                return -1
                
            mid_idx = (s_idx + e_idx) // 2
            if target == nums[mid_idx]:
                    return mid_idx
            elif target < nums[mid_idx]:
                return divide(s_idx, mid_idx - 1)
            else:
                return divide(mid_idx + 1, e_idx)
        
        return divide(0, 5)