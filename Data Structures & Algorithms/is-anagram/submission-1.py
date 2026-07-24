class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        text1={}
        for ch in s:
            text1[ch]=text1.get(ch,0)+1
        
        for ch in t:
            text1[ch]=text1.get(ch,0)-1
        
            if text1[ch]<0:
                return False
        return True