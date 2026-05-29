class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hmS = {}
        hmT = {}

        for i in range(len(s)):
            hmS[s[i]] = 1 + hmS.get(s[i], 0)
            hmT[t[i]] = 1 + hmT.get(t[i], 0)
        
        for c in hmS:
            if hmS[c] != hmT.get(c, 0):
                return False
                
        return True