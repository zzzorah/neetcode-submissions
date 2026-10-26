class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s_idx = 0
        e_idx = len(nums) - 1

        while s_idx <= e_idx:
            m_idx = s_idx + (e_idx - s_idx) // 2

            if target == nums[m_idx]:
                return m_idx
            elif target < nums[m_idx]:
                e_idx = m_idx - 1
            else:
                s_idx = m_idx + 1
        
        return -1