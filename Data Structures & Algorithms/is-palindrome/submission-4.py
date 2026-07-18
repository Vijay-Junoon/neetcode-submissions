class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s:
            if i.isalnum():
                word += i.lower()
        
        rev_word = word[::-1]
        if rev_word == word:
            return True
        else:
            return False