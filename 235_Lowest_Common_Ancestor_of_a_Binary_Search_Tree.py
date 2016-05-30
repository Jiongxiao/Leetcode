# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val>q.val:
        	p,q=q,p
        node=root
        while(node is not None):
        	if node.val<=q.val and node.val>=p.val:
        		return node
        	if node.val>p.val:
        		node=node.left
        	else:
        		node=node.right
        return node

