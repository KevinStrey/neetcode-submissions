class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        p1 = 0
        p2 = len(s)-1
        while p1 < p2:
            if(s[p1] != s[p2]):
                return False
            p1 = p1+1
            p2 = p2-1
        return True
