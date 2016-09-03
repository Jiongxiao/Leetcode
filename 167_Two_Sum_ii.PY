class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        size=len(numbers)
        for i in range(size):
            j=i+1
            k=size-1
            index=binarySearch(j,k,target-numbers[i],numbers)
            if index:
                result=[i+1,index+1]
                break
        return result
def binarySearch(j,k,x,data):
    if data[j]==x:
        return j
    elif data[k]==x:
        return k
    else:
        mid=(j+k)/2
        if mid==j or mid==k:
            return
        if data[mid]==x:
            return mid
        else:
            if data[mid]<x:
                j=mid
                return binarySearch(j,k,x,data)
            if data[mid]>x:
                k=mid
                return binarySearch(j,k,x,data)