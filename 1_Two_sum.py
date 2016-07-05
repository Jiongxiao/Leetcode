class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic=dict()
        for i in range(len(nums)):
        	dic[nums[i]]=[]
        for i in range(len(nums)):
        	dic[nums[i]].append(i)
        for i in dic.keys():
        	index1=dic[i][0]
        	if len(dic[i])<2:
        		dic.pop(i)
        	else:
        		dic[i].pop(0)
        	if (target-i) in dic:
        		result=[index1,dic[target-i][0]]
        return result

####太特么机智了!!!
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in range(len(nums)):
        	if(nums[i] in dic):
        		return[i,dic[nums[i]]]
        	else:
        		dic[target-nums[i]]=i