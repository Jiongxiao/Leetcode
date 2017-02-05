class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        res=set()
        if n<2:
            return []
        self.helper(res,nums,[],0)
        return [list(t) for t in res]
    def helper(self,res,nums,l,count):
        if count==len(nums):
            if len(l)>=2:
                res.add(tuple(l))
            return
        a=l[:]
        b=l[:]
        self.helper(res,nums,a,count+1)
        if not l or nums[count]>=l[-1]:
            b.append(nums[count])
            self.helper(res,nums,b,count+1)