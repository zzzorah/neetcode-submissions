# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        min = None
        max = None

        def countHeight(node: TreeNode, count: int):
            nonlocal min, max
            if node is None:
                if min is None or count < min:
                    min = count
                if max is None or count > max:
                    max = count
            else:
                countHeight(node.left, count + 1)
                countHeight(node.right, count + 1)
        
        countHeight(root, 0)
        if max is None or (max - min) <= 1:
            return True
        else: return False