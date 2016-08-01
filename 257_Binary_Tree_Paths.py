# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  ##这玩意不对！
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
    	if not root:
    		return []
    	result=[]
    	from collections import deque
    	import copy

    	stack=deque([root])
    	p=root.left
    	pathQueue=deque([root])

    	def getPath(stack):
    		path=str(stack.popleft().val)
    		while(stack):
    			p=stack.popleft()
    			path=path+'->'+str(p.val)
    		return path

    	while(True):
    		while (p):
    			stack.append(p)
    			pathQueue.append(p)
    			p=p.left
    		if not stack:
    			break
    		p=stack.pop()
    		if p.right:
    			p=p.right
    		else:
    			result.append(getPath(pathQueue))
    			pathQueue=copy.deepcopy(stack)
    			p=None
    	return result


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
		

	def binaryTreePaths(self, root):

		def getPath(node,path):
			if not node.left and not node.right:
				result.append(path+str(node.val))
			if node.left:
				getPath(node.left,path+str(node.val)+'->')
			if node.right:
				getPath(node.right,path+str(node.val)+'->')
		
		if not root:
			return []
		result=[]
		path=''
		getPath(root,path)
		return result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  ##这玩意可以！
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):		






