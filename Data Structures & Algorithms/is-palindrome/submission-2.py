class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string = s.replace(' ','')

        string = ''.join(char for char in s if char.isalnum())
        string = string.lower()

        for i in range(0, round(len(string)/2)):
            end = (len(string)-1)-i
            if string[i] != string[end]:
                return False

        return True

            
        
