class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        ls=len(s)
        lt=len(t)
        i=j=0
        while(j<lt):
            if s[i]==t[j]:
                if i==ls-1:
                    return True
                i+=1
                j+=1
            else:
                j+=1
        return False
        