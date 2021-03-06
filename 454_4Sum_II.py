class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        n=len(A)
        if not n:
            return 0
        l1=[]
        l2=[]
        for i in range(n):
            for j in range(n):
                l1.append(A[i]+B[j])
                l2.append(C[i]+D[j])
        dic=dict()
        res=0
        for i in range(n*n):
            dic[l1[i]]=dic.get(l1[i],0)+1
        for i in range(n*n):
            res+=dic.get(-l2[i],0)
        return res

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        n=len(A)
        if not n:
            return 0
        dic=dict()

        for i in range(n):
            for j in range(n):
                num1=(A[i]+B[j])
                dic[num1]=dic.get(num1,0)+1        
        res=0
        for i in range(n):
            for j in range(n):
                num2=(C[i]+D[j])
                res+=dic.get(-num2,0)
        return res
