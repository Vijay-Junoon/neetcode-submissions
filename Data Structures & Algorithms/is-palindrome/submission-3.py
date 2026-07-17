class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s = ''.join([i for i in s if i.isalnum()])
        s = s.lower()
        return s == s[::-1]
