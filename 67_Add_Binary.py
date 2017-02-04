class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l=len(a)
        r=len(b)
        a=a[::-1]
        b=b[::-1]
        i=j=0
        rem=0
        res=[]
        while(i<l or j<r):
            if i<l:
                left=a[i]
            else: left=0
            if j<r:
                right=b[j]
            else: right=0
            summ=int(left)+int(right)+rem
            res.append(str(summ%2))
            rem=summ/2
            i+=1
            j+=1
        if rem:
            res.append(str(rem))
        res.reverse()
        return ''.join(res)


