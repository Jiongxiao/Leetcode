class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bit=0
        mi=min(nums)
        for i in range(len(nums)):
        	nums[i]+=abs(mi)
        	temp=int(1<<nums[i])
        	if bit&temp != 0:
        		bit-=temp
        	else:
        		bit+=temp
        result=[]
        bitStr=bin(bit)[::-1]
        for i in range(len(bitStr)):
        	if bitStr[i]=='1':
        		result.append(i-abs(mi))
        return result
############  memory exceeded  ###########

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bit=reduce(lambda x,y: x^y, nums)  #找到两个不重复的数
        bit&=~bit+1   #A&(-A)可以得到A中第一个不为0的位，用来区分剩下的两个数
        result=[0,0]
        for i in nums:
        	if bit&i==0:
        		result[0]^=i
        	else:
        		result[1]^=i
        return result