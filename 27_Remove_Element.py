class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ##   1342782435  2 
        back=0
        n=len(nums)
        front=n-1

        while back<=front:
            while(back<n and nums[back]!=val):
                back+=1
            while front>=0 and nums[front]==val:
                front-=1
            if back<front:
                nums[back],nums[front]=nums[front],nums[back]
        return front+1
        

