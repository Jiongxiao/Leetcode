# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []
        result=[]
        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        return result



class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []

        result=[]
        from collections import deque

        p=root
        pStack=deque()
        stageStack=deque()
        s=0
        while (True):
        	while(p):
        		pStack.append(p)
        		stageStack.append(0)
        		p=p.left

        	if not stageStack:
        		break
        	s=stageStack.pop()
        	if s==0:
        		stageStack.append(1)
        		p=pStack.pop()
        		pStack.append(p)
        		p=p.right
        	else:
    			p=pStack.pop()
    			result.append(p.val)
    		
    			p=None  ####toooooooo TM important!!!!!!!!!

        return result
	        

	        	




