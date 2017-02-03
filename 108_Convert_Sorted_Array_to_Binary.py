# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.build(nums,0,len(nums)-1)
    def build(self,nums,start,end):
        if start>end:
            return None
        n=end-start+1
        mid=(n+1)/2-1+start
        root=TreeNode(nums[mid])
        root.left=self.build(nums,start,mid-1)
        root.right=self.build(nums,mid+1,end)
        return root