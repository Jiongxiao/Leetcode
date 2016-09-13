class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums=nums
        self.size=len(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import copy
        import random
        n=0
        result=copy.deepcopy(self.nums)
        while n<self.size:
            i=random.randint(0,n)
            result[i],result[n]=result[n],result[i]   ###Fisher–Yates shuffle algorithm
            n+=1
        return result





