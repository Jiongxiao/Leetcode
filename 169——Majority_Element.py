class Solution(object):  #O(nlgn)
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet={}
        for num in nums:
        	numSet[num]=numSet.get(num,0)+1

        sortedList=sorted(numSet.items(),key=lambda x: x[1],reverse=True)
        return sortedList[0][0]

##高级方法 O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        major=nums[0]
        for num in nums:
        	if num==major:
        		count+=1
        	else:
        		count-=1
        	if count<0:
        		major=num
        		count=1
        return major

