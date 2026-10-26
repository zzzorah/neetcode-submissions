class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        def divide(s_idx:int, e_idx:int):
            if s_idx == e_idx and target != nums[s_idx]:
                return -1
                
            mid_idx = s_idx + (e_idx - s_idx) // 2
            if target == nums[mid_idx]:
                    return mid_idx
            elif target < nums[mid_idx] and mid_idx != 0:
                return divide(s_idx, mid_idx - 1)
            elif target > nums[mid_idx] and mid_idx != length -1:
                return divide(mid_idx + 1, e_idx)
            else:
                return -1
        
        return divide(0, len(nums) - 1)