class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return nums[0]
        left=0
        right=n-1
        while True:
            if left==right:
                return nums[left]
            mid=(left+right)/2
            if nums[mid]>=nums[left] and nums[mid]>=nums[right]:
                left=mid+1
            elif nums[left]>nums[right]:
                left=left
            else: return nums[left]


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return nums[0]
        left=0
        right=n-1
        while left<right:
            mid=(left+right)/2
            if nums[mid]<nums[right]:
                right=mid
            else:
                left=mid+1
        return nums[left]