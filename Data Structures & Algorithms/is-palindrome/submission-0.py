class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i = i + 1
                continue
            if not s[j].isalnum():
                j = j - 1
                continue
            if s[i].lower() == s[j].lower() and len(s) != 0:
                i = i + 1
                j = j - 1
            else:
                return False

        return True 
        