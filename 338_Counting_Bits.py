class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result=[0]
        if num==0:
            return result
        flag=1
        for i in range(1,num+1):
            if i==flag:
                result.append(1)
                flag*=2
            else:
                if i<flag*3/4:
                    result.append(result[i-flag/4])
                else:
                    result.append(result[i-flag/4]+1)
        return result
