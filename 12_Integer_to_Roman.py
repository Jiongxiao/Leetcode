class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        sta=[["","I","II","III","IV","V","VI","VII","VIII","IX"],\
        ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],\
        ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],\
        ["","M","MM","MMM"]]
        base=[1000,100,10,1]
        result=''
        for i in range(4):
        	result+=(sta[3-i][num/base[i]%10])
        return result





