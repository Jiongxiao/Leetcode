# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftDepth=maxDepth(self, root.left)
        rightDepth=maxDepth(self, root.right)
        return max(leftDepth,rightDepth)+1
        
