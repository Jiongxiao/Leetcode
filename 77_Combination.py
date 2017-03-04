class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n<k or k==0:
            return []
        res=[]
        self.get_number([],1,n,k,res)
        return res
    def get_number(self,l,start,end,k,res):
        if start>end+1:
            return 
        if len(l)==k:
            res.append(l)
        else:
            ll=l[:]
            rr=l+[start]
            self.get_number(ll,start+1,end,k,res)
            self.get_number(rr,start+1,end,k,res)

#####居然超时了！！！！！



class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n<k or k==0:
            return []
        res=[]
        self.get_number([],1,n,k,res)
        return res
    def get_number(self,l,start,end,k,res):
        if k==0:
            res.append(l)
            return
        for i in range(start,end+1):
            new_l=l+[i]
            self.get_number(new_l,i+1,end,k-1,res)
            
