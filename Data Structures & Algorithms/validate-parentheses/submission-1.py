class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False 
        stack = []
        d = {')':'(',']':'[','}':'{'}
        cnt = 0
        for i in s:
            if i not in d:
                stack.append(i)
            else:
                if stack:
                    if stack[-1] == d[i]:
                        stack.pop()
                        cnt+=1
                    else:
                        return False
        if cnt == len(s)//2:
            return True
        return False