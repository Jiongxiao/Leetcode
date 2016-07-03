class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1=dict();
        result=[]
        for i in nums1:
        	dic1[i]=1
        for j in set(nums2):
        	if j in dic1:
        		result.append(j)
        return result
