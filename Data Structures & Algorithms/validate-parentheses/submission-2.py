class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for ch in s:
            if ch not in brackets:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] != brackets[ch]:
                    return False
                stack.pop()

        return True if not stack else False

        
 