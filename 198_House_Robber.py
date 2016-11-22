class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n=len(nums)
        if n==1:
            return nums[0]
        last=0
        now=0

        for i in range(n):
            temp=last
            last=now
            now=max(temp+nums[i],now)
        return now