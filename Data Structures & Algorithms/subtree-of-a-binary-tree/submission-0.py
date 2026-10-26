# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def findRoot(node:TreeNode):
            if node is None:
                return None

            if node.val == subRoot.val:
                return node
            else:
                return findRoot(node.left) or findRoot(node.right)

        def isSame(node: TreeNode, target: TreeNode):
            if node is None and target is None:
                return True
            if node is None or target is None:
                return False
           
            if node.val != target.val:
                return False
            else:
                return isSame(node.left, target.left) and isSame(node.right, target.right)

        node = findRoot(root)
        if node is not None:
            return isSame(node, subRoot)
        else: return False

        