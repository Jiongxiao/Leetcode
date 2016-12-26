# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
            """
        if not root:
            return 0
        if (not root.left )and (not root.right):
            return root.val
        if root.left:
            left=self.rob(root.left.left)+self.rob(root.left.right)
        else: left=0
        if root.right:
            right=self.rob(root.right.left)+self.rob(root.right.right)
        else: right=0
        if (root.val+left+right)>(self.rob(root.left)+self.rob(root.right)):
            return root.val+left+right
        else:
            return self.rob(root.left)+self.rob(root.right)