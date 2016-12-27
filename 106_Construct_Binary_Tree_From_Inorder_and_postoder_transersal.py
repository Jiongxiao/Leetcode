# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): ## memory exceed!!!  ??????why   postorder[0:i] too many times vs postorder always the original one
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        root=TreeNode(postorder[-1])
        n=len(inorder)
        for i in range(n):
            if inorder[i]==root.val:
                break
        root.left=self.buildTree(inorder[0:i],postorder[0:i])
        root.right=self.buildTree(inorder[i+1:],postorder[i:-1])
        return root


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder or not inorder:
            return None
        root=TreeNode(postorder.pop())
        i=inorder.index(root.val)
        root.right=self.buildTree(inorder[i+1:],postorder)
        root.left=self.buildTree(inorder[0:i],postorder)
        return root


        