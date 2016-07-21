class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        j=len(s)-1
        vowels=set('aoeiuAOEIU')
        result=['']*len(s)
        while(i<j):
        	if s[i] not in vowels:
        		result[i]=s[i]
        		i+=1
        	else:
        		if s[j] not in vowels:
        			result[j]=s[j]
        			j-=1
        		else:
        			result[i],result[j]=s[j],s[i]
        			i+=1
        			j-=1
        if i==j:
        	result[i]=s[i]
        return ''.join(result)
