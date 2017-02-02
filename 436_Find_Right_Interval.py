# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        n=len(intervals)
        array=[]
        for i in range(n):
            array.append([intervals[i].start,i])
        array.sort()
        res=[]
        for j in range(n):
            index=self.search(intervals[j].end,array)
            res.append(index)
        return res


    def search(self,num,array):
        min=0
        max=len(array)-1
        if min>max:
            return -1
        if num>array[max][0]:
            return -1
        while min<max:
            m=(min+max)/2
            if array[m][0]<num:
                min=m+1
            elif array[m][0]>num:
                max=m-1
            else:
                return array[m][1]
        if array[min][0]<num:
            return array[min][1]+1
        else:
            return array[min][1]
