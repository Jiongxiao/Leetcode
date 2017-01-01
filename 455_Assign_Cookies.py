class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        if not s:
            return 0
        res=0
        i=j=0
        while(j<len(s) and i<len(g)):
            if g[i]<=s[j]:
                res+=1
                i+=1
                j+=1
            else:
                j+=1
        return res
