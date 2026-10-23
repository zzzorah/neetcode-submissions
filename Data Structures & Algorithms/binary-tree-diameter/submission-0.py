# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_value = 0

        def findMax(node: Optional[TreeNode]) -> int:
            nonlocal max_value

            if not node:
                return 0

            leftMax, rightMax = findMax(node.left), findMax(node.right)

            if (leftMax + rightMax) > max_value:
                max_value = leftMax + rightMax

            return max(leftMax, rightMax) + 1


        findMax(root)
        return max_value