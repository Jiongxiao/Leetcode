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


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rty
        """
        for i in range(len(numbers)):
            # if i>0 and numbers[i-1]==numbers[i]:
            #     continue      
            ## skipping duplicates made the code run much faster
            l=i+1
            r=len(numbers)-1
            while(l<=r):
                mid=(l+r)/2
                if target-numbers[i]== numbers[mid]:
                    return [l+1,mid+1]
                elif target-numbers[i]< numbers[mid]:
                    r=mid-1
                else:
                    l=mid+1


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rty
        """
        l=0
        r=len(numbers)-1
        while(l<r):
            if numbers[l]+numbers[r]==target:
                break
            elif numbers[l]+numbers[r]<target:
                l+=1
            else: r-=1
        if l>=r:
            return []
        else: return [l+1,r+1]



