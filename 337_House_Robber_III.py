# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):  ##too many calling rob!!!! time!!!!
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
        l=self.rob(root.left)
        r=self.rob(root.right)
        if root.val+left+right>l+r:
            return root.val+left+right
        else:
            return l+r



class Solution(object):  
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
            """

        '''

        f1(node) be the value of maximum money we can rob from the subtree with node as root ( we can rob node if necessary).

        f2(node) be the value of maximum money we can rob from the subtree with node as root but without robbing node.

        Then we have

        f2(node) = f1(node.left) + f1(node.right) and

        f1(node) = max( f2(node.left)+f2(node.right)+node.value, f2(node) ).
        '''
        return max(self.robDF(root))
    def robDF(self,node):  ## res[0] without the current node; res[0] using the current node
        if not node:
            return (0,0)

        left=self.robDF(node.left)
        right=self.robDF(node.right)
        res=(0,0)
        res[0]= max(left[0],left[1])+max(right[0],right[1])
        res[1]= left[0]+right[0]+node.val
        return res







