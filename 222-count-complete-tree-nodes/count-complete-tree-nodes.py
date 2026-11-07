# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        left=root
        right=root
        lefth=0
        righth=0
        while left:
            lefth+=1
            left=left.left
        while right:
            righth+=1
            right=right.right
        if lefth==righth:
            return (2**lefth)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
