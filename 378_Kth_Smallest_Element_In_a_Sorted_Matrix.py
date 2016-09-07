class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n=len(matrix)
        l,r=matrix[0][0],matrix[n-1][n-1]
        while(l<r):
            mid=(l+r)/2
            if self.findNumsSmallerThanX(matrix,n,mid)<k:
                l=mid+1
            else: r=mid
        return l



    def findNumsSmallerThanX(self,matrix,n,x):
        i=0
        j=n-1
        cnt=0
        while(i<n and j>=0):
            if matrix[i][j]<=x:
                i+=1
                cnt+=j+1
            else:
                j-=1
        return cnt
######nlog(X)



class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n=len(matrix)
        heap=[]
        for i in range(n):
            heap.append((matrix[0][i],0,i))
        heapq.heapify(heap)
        for i in range(k):
            val,r,c=heapq.heappop(heap)
            if r<n-1:
                heapq.heappush(heap,(matrix[r+1][c],r+1,c))
        return val
#klog(n)

