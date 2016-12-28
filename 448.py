class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[abs(nums[i])-1]=-abs(nums[abs(nums[i])-1])
        return [j+1 for j in range(len(nums)) if nums[j]>0]