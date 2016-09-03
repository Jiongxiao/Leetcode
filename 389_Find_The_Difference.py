class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        for j in t:
            if j not in dic:
                return j
            else:
                dic[j]-=1
                if dic[j]==0: del dic[j]
        
