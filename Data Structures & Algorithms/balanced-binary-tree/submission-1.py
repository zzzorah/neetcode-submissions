# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        def countHeight(node: TreeNode, count: int):
            nonlocal result

            if node is None:
                return count
            else:
                leftCount = countHeight(node.left, count + 1)
                rightCount = countHeight(node.right, count + 1)
                
                print(f'node({node.val}) leftH={leftCount} rightH={rightCount} return={max(leftCount, rightCount)}')

                if abs(leftCount - rightCount) > 1:
                    result = False

                return max(leftCount, rightCount)


        countHeight(root, 0)
        return result
        