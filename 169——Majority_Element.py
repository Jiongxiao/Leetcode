class Solution(object):
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
