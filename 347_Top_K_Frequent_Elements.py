class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dataSet={}
        for i in nums:
            dataSet[i]=dataSet.get(i,0)+1
        sortedData=sorted(dataSet.iteritems(),key=lambda x: x[1],reverse=True)
        result=[]
        for j in range(k):
            result.append(sortedData[j][0])
        return result
