# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):  ###recursion
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []
        result=[]
        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        return result

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []
        result=[]
        from collections import deque
        stack=deque([root])
        while(stack):
        	p=stack.pop()
        	result.append(p.val)
        	if p.right:
        		stack.append(p.right)
        	if p.left:
        		stack.append(p.left)
        return result

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []
        result=[]
        from collections import deque

        stack=deque()
        p=root
        while(True):
        	result.append(p.val)
        	q=p.right
        	if q:
        		stack.append(q)
        	p=p.left
        	if not p:
        		if not stack:
        			break
        		p=stack.pop()
        return result

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result=[]
        from collections import deque

        stack=deque()
        p=root
        while(stack or p):
            if p:
                result.append(p.val)
                stack.append(p)
                p=p.left
            else:
                p=stack.pop()
                p=p.right
        return result
