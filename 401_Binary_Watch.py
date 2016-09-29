class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res=[]
        for h in range(12):
        	for m in range(60):
        		time=h*64+m
        		if self.popCount(time)==num:
        			res.append("%d:%02d" %(h,m))
        return res
    
    def popCount(self,n):
    	return bin(n).count('1')


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res=[]
        self.help(num,0,0,0,res)
        return res

    def help(self,num,pos,hour,minute,res):
    	if hour>11 or minute>59:
    		return
    	if num==0:
    		res.append("%d:%02d" %(hour,minute))
    	for i in range(pos,10):
    		if i<=3:
    			self.help(num-1,i+1,hour+(1<<(3-i)),minute,res)
    		else:
    			self.help(num-1,i+1,hour,minute+(1<<(9-i)),res)