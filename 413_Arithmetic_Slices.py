class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        if n<3:
            return 0
        res=0
        tail=[0]*n
        if A[2]+A[0]==A[1]<<1:
            tail[2]=1
            res+=1

        for i in range(3,n):
            if A[i]+A[i-2]==A[i-1]<<1:
                tail[i]=tail[i-1]+1
                res+=tail[i]
        return res
