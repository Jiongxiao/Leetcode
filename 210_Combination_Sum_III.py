class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k<=0:
            return 
        if k==1:
            if 0<n<10:
                return[[n]]
            else: return 
        res=[]
        for i in range(1,10):
            rr=self.help(k,n,i)
            if rr:
                res.extend(rr)
        return res
    def help(self,k,n,start):
        if n<start:
            return
        if k==1:
            if n==start:
                return [[n]]
            else: return
        re=[]
        for j in range(start+1,10):
            imme=self.help(k-1,n-start,j)
            if imme:
                for l in imme:
                    re.append([start]+l)
        return re






