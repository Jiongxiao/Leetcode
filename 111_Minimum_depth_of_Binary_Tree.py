# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        from collections import deque

        level=0
        queue=deque([root])
        while(True):
            level+=1
            for i in range(len(queue)):
                p=queue.popleft()
                if not p.left and not p.right:
                    return level
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
        return result



                



