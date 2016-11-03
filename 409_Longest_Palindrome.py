class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
        	return 0
        dic=dict()
        result=0
        for i in s:
        	if i in dic:
        		result+=2
        		del dic[i]
        	else:
        		dic[i]=1
        if  dic:
        	result+=1
        return result

