# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        diff=self.depth(root.left)-self.depth(root.right)
        if diff<=1 and diff>=-1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else: return False
        
        
    def depth(self,node):
        if not node:
            return 0
        from collections import deque
        depth=0
        queue=deque([node])
        while(queue):
            depth+=1
            for i in range(len(queue)):
                p=queue.popleft()
                # if not p.left and not p.right:
                #     return depth
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
        return depth
    