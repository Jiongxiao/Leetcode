# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
        	return []
        
        from collections import deque
        result=[]
        queue=deque([root])
        while(queue):
        	level=[]
        	for i in range(len(queue)):
        		p=queue.popleft()
        		level.append(p.val)
        		if p.left:
        			queue.append(p.left)
        		if p.right:
        			queue.append(p.right)
        	result.append(level)
        return result
