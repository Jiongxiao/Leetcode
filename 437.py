# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        res=dict()
        from collections import deque
        st=deque()
        st.append([root,{-3000000:1}])
        while(st):
            node,map1=st.pop()
            if node:
                new_map=dict()
                for key in map1.keys():
                    new_map[key+node.val]=map1.get(key)
                new_map[node.val]=new_map.get(node.val,0)+1
                for key in new_map.keys():
                    res[key]=res.get(key,0)+new_map[key]
                    # print key,new_map[key]
                st.append([node.right,new_map])
                st.append([node.left,new_map])
        return res.get(sum,0)

