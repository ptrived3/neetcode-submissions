class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = "".join(char for char in s if char.isalnum())
        endIndx = len(cleanS) - 1

        for i in range(len(cleanS)//2):
            if cleanS[i].upper() != cleanS[endIndx-i].upper():
                return False

        return True