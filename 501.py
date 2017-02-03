# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.curVal=0
        self.res=[]
        self.maxcount=0
        self.count=0

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorder(root)
        return self.res

    def inorder(self,node):
        if not node:
            return
        self.inorder(node.left)
        print node.val,self.curVal
        if (node.val!=self.curVal):
            self.count=0
            self.curVal=node.val
            print 'self.curVal', self.curVal
        self.count+=1
        print 'self.count=', self.count
        if (self.count==self.maxcount):
            self.res.append(self.curVal)
        elif self.count>self.maxcount:
            print self.curVal
            del self.res[:]
            self.res.append(self.curVal)
            self.maxcount=self.count
        self.inorder(node.right)

 
