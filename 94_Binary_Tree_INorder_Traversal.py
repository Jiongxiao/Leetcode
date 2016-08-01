# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []
        result=[]
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result



class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []
        result=[]
        from collections import deque

        p=root
        stack=deque()
        while(True):
        	while(p):
        		stack.append(p)
        		p=p.left
        	if not stack:
        		break
        	p=stack.pop()
        	result.append(p.val)
        	p=p.right
        	

        return result


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []
        result=[]
        from collections import deque

        p=root
        stack=deque()
        while(stack or p):
        	if p:
        		stack.append(p)
        		p=p.left
        	else:
        		p=stack.pop()
        		result.append(p.val)
        		p=p.right
        return result


