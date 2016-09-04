class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic={}
        for ch in magazine:
            dic[ch]=dic.get(ch,0)+1
        for ch in ransomNote:
            if ch not in dic:
                return False
            else:
                dic[ch]-=1
                if dic[ch]==0:
                    del dic[ch]
        return True
