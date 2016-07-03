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

###########################################
class Solution(object):
    def findDuplicate(self, nums):
        result=0
        for i in nums:
            if result&(1<<i):return i
            result+=(1<<i)
########很机智啊！但是为啥时间跟上面差不多啊

nums=[1,2,3,4,5,6,2]
result =0 
for i in nums:
    print bin(result), 1<<i, result&(1<<i)
    if result&(1<<i): print i
    result+=(1<<i)