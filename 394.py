class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        num=''
        stack.append(['',1])
        for ch in s:
            if ch.isdigit():
                num+=ch
            elif ch=='[':
                stack.append(['',int(num)])
                num=''
            elif ch==']':
                temp, count= stack.pop()
                stack[-1][0]+=temp*count
            else:
                stack[-1][0]+=ch
        return stack[-1][0]


