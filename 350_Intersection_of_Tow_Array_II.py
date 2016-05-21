class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        result=[]
        i=0;j=0
        while i<len(nums1) and j<len(nums2):
        	if nums1[i]==nums2[j]:
        		result.append(nums2[j])
        		i+=1
        		j+=1
        	elif nums1[i]<nums2[j]:
        		i+=1
        	else: j+=1
        return result


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1={}
        dic2={}
        for num in nums1:
        	dic1[num]=dic1.get(num,0)+1
        for num in nums2:
        	dic2[num]=dic2.get(num,0)+1
        list1=dic1.items()
        list2=dic2.items()
        i=0;j=0
        result=[]
        while i<len(list1) and j<len(list2):
        	if list1[i][0]==list2[j][0]:
        		for k in range(min(list1[i][1],list2[j][1])):
        			result.append(list1[i][0])
        		i+=1
        		j+=1
        	elif list1[i][0]<list2[j][0]:
        		i+=1
        	else:j+=1
        return result

nums1=[4,7,9,7,6,7]
nums2=[5,0,0,6,1,6,2,2,4]

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1={}
        result=[]
        for num in nums1:
        	dic1[num]=dic1.get(num,0)+1
        for i in nums2:
        	if dic1.get(i,0)>0:
        		result.append(i)
        		dic1[i]-=1
        return result
#理论上来说方法二的复杂度应该比较好，但是oj时间却更长！
