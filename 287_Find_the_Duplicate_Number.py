class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        buf=0
        a=nums[0]
        while(nums[buf]!=buf):
        	a=nums[buf]
        	nums[buf]=buf
        	buf=a
        return a
        ######这个方法非常牛逼，时间复杂度只要O(n)，但是题目要求不能改变list
        