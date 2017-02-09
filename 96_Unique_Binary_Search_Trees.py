class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 1
        if n<=2: return 2
        res=[0]*(n+1)
        res[0]=1
        res[1]=1
        res[2]=2
        for i in range(3,n+1):
            for j in range(1,i+1):
                res[i]=res[i]+res[j-1]*res[i-j]
        return res[n]
