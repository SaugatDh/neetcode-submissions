from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Frequency counter / Hashmap
        if len(s)!=len(t):
            return False
        
        count = {}

        for char in s:
            count[char] = count.get(char,0)+1 # Get he frequency
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char]-=1
        
        return True

        # return Counter(s)==Counter(t)
        # return sorted(s)==sorted(t)