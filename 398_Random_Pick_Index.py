class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums=nums
        self.pool=0
        self.index=0
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        self.pool=0
        self.index=0
        for i in range(len(self.nums)):
            if self.nums[i]==target:
                self.pool+=1
                p=random.randint(1,self.pool)
                if p==1:
                    self.index=i
        return self.index

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)