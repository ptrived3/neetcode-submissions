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
            if c not in hmT or hmT[c] != hmS[c]:
                return False
        
        for c in hmT:
            if c not in hmS or hmT[c] != hmS[c]:
                return False
        
        return True

