# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
        	return True
        l=root.left
        r=root.right
        if not l and not r:
        	return True
        if l and r:
        	if l.val==r.val:
        		newroot1=l
        		newroot1.right=r.right
        		newroot2=r
        		newroot2.r=l.right
        		return self.isSymmetric(newroot2) and self.isSymmetric(newroot1)
        		# l.right,r.right=r.right,l.right
        		# return self.isSymmetric(r) and self.isSymmetric(l)
        	else:
        		return False
        return False

########上面这个是不对的，引用的问题很容易被搞错！！！

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import copy
        if not root:
        	return True
        l=root.left
        r=root.right
        if not l and not r:
        	return True
        if l and r:
        	if l.val==r.val:
        		newroot1=copy.copy(l)
        		newroot1.right=r.right
        		newroot2=copy.copy(r)
        		newroot2.right=l.right
        		return self.isSymmetric(newroot2) and self.isSymmetric(newroot1)
        	else:
        		return False
        return False

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
        	return True
        from collections import deque

        queue=deque([root])
        while(queue):
        	level=[]
        	for i in range(len(queue)):
        		p=queue.popleft()
        		if p:
        			level.append(p.val)
        			queue.append(p.left)
        			queue.append(p.right)
        		else: level.append(None)
        	if list(reversed(level))!=level:
        		return False
        return True
        		
