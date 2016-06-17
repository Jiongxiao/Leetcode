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


##########O(lgn) 时间好像不是很好      
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findD(start,end):
            mid=(start+end)/2
            m=0
            l=0
            s=0
            for i in nums:
                if start<=i and i <mid:
                    s+=1
                elif mid<i and i<=end:
                    l+=1
                elif mid==i:
                    m+=1
            if m>=2:
                return mid
            else:
                if s>=l:
                    return findD(start, mid-1)
                else:
                    return findD(mid+1, end)
        return findD(1,len(nums)-1)