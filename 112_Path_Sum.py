# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

##########BFS  
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        from collections import deque

        queue=deque([(root,0)])
        while(queue):
            node,pathSum=queue.popleft()
            pathSum+=node.val
            if not node.left and not node.right:
                if pathSum==sum:
                    return True
            if node.left:
                queue.append((node.left,pathSum))
            if node.right:
                queue.append((node.right,pathSum))
        return False


#########DFS 

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        from collections import deque

        stack=deque()
        node=root
        pathSum=0
        while(True):
            
            while(node):
                pathSum+=node.val
                stack.append((node,pathSum))
                node=node.left
            if not stack:
                return False
            node,pathSum=stack.pop()
            if not node.right and not node.left:
                print pathSum
                if pathSum==sum:
                    return True
            node=node.right

#########DFS 
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        from collections import deque

        stack=deque([(root,0)])
        while(stack):
            node,pathSum=stack.pop()
            pathSum+=node.val
            if not node.left and not node.right:
                if pathSum==sum:
                    return True
            if node.right:
                stack.append((node.right,pathSum))
            if node.left:
                stack.append((node.left,pathSum))
        return False





