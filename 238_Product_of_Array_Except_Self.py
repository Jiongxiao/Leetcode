class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size=len(nums)
        output=[1]*size
        output[0]=1
        for i in range(1,size):
        	output[i]=output[i-1]*nums[i-1]  #calculate the multiplication of all the left nums of nums[i]
        temp=1
        for j in range(size-1,-1,-1):
        	output[j]*=temp
        	temp*=nums[j]   # the multiplication of all the right nums of nums[j]
        return output

class Solution(object):   # time limit exceeded!!!
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size=len(nums)
        output=[1]*size
        for i in range(size):
        	for j in range(size):
        		if i==j:
        			continue
        		output[i]*=nums[j]
        return output


