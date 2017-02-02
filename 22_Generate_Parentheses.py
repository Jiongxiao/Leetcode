class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        from collections import deque
        if not n:
            return [""]
        res=deque()
        res.append(["",0])
        for i in range(2*n):
            length=len(res)
            for j in range(length):
                s,b=res.popleft()
                for ch in '()':
                    new_b=b
                    temp=s+ch
                    if ch=='(':
                        new_b+=1
                    else:
                        new_b-=1
                    if new_b>=0 and new_b<=n:
                        res.append([temp,new_b])
        result=[]
        while (res):
            tur=res.popleft()
            if tur[1]==0:
                result.append(tur[0])
        return result

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.backtract(res,'',0,0,n)
        return res
    def backtract(self,res, s, left, right, n):
        if (len(s)==2*n):
            res.append(s)
            return

        if left<n:
            self.backtract(res,s+'(',left+1,right,n)
        if left>right:
            self.backtract(res,s+')', left, right+1,n)





