class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """

        front=1
        n=len(str)
        first=str[0]
        while True:
            while front<n:
                if str[front]!=first or n%(front)!=0:
                    front+=1
                else: break
            if front>=n:
                return False
            for i in range(1,n/front):
                if str[0:front]!=str[i*front:(i+1)*front]:
                    front+=1
                    break
                if i==n/front-1:
                    return True


class Solution(object):   ##reference
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        ss=(str+str)[1:-1]
        return ss.find(str)!=-1




        
