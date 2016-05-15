class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # def getDic(s):
        # 	dic={}
        # 	for i in s:
        # 		dic[i]=dic.get(i,0)+1
        # 	return dic
        
        # return getDic(s)==getDic(t)

        if len(s)!=len(t):
            return False
        else:
            sumS=0;sumT=0
            for i in range(len(t)):
                charS=ord(s[i])
                charT=ord(t[i])
                sumS+=charS*(charS-1)*(charS-2)
                sumT+=charT*(charT-1)*(charT-2)
            return sumT==sumS
