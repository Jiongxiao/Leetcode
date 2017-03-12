class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        n=len(nums)
        res=[[]]
        for i in range(n):
            new_res=res[:]
            for l in res:
                new_l=l[:]
                new_l.append(nums[i])
                new_res.append(new_l)
            res=new_res
        return res