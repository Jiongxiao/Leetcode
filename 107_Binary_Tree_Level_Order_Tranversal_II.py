# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
        	return []
        stack=[0]*(100000)
        front=rear=0
        newLevel=1   #denotes the position of the first node of every level
        result={}
    	stack[rear]=root
    	rear+=1
    	rank=1
    	result[rank]=[]
    	while(front<rear):
    		p=stack[front]
    		result[rank].append(p.val)
    		front+=1
    		if p.left:
    			stack[rear]=p.left
    			rear+=1
    		if p.right:
    			stack[rear]=p.right
    			rear+=1
    		if (front==newLevel):
    			newLevel=rear
    			rank+=1
    			result[rank]=[]
    	r=[]
    	result=sorted(result.items(),reverse=True)
    	for i in result:
    		r.append(i[1])
    	r.pop(0)
    	return r


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
        	return []

        from collections import deque

        result = deque()
        stack = deque([root])
        while(stack):
        	level=[]
        	for i in range(len(stack)):
        		front=stack.popleft()
        		level.append(front.val)
        		if front.left:
        			stack.append(front.left)
        		if front.right:
        			stack.append(front.right)
        	result.appendleft(level)
        return list(result)


class Solution(object):   ## update the first solution
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
        	return []
        stack=[0]*(100000)
        front=rear=0
        newLevel=1   #denotes the position of the first node of every level
    	stack[rear]=root
    	rear+=1
    	result=[]
    	level_r=[]
    	while(front<rear):
    		p=stack[front]
    		level_r.append(p.val)
    		front+=1
    		if p.left:
    			stack[rear]=p.left
    			rear+=1
    		if p.right:
    			stack[rear]=p.right
    			rear+=1
    		if (front==newLevel):
    			newLevel=rear
    			result.append(level_r)
    			level_r=[]
    	result.reverse()
    	return result









        	


